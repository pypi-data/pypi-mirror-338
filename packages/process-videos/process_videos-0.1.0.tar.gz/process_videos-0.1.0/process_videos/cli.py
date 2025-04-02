import os
import subprocess
import click
import shutil

def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg is not installed or not available in your system PATH.")

@click.command()
@click.option('--dir', 'directory', required=True, type=click.Path(exists=True, file_okay=False), help='Directory containing the videos to process')
@click.option('--codec', default='libx264', help='Video codec (libx264 or libx265)')
@click.option('--crf', default='28', help='CRF value for video compression (higher = more compression)')
@click.option('--preset', default='veryfast', help='Encoder speed preset (ultrafast, veryfast, fast, etc)')
@click.option('--audio-bitrate', default='128k', help='Audio bitrate (e.g., 128k)')
def main(directory, codec, crf, preset, audio_bitrate):
    check_ffmpeg()

    def extract_audio(video_path, audio_path):
        subprocess.run([
            "ffmpeg", "-y", "-i", video_path,
            "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "1", audio_path
        ], check=True)

    def normalize_audio_ffmpeg(audio_path, treated_path):
        subprocess.run([
            "ffmpeg", "-y", "-i", audio_path,
            "-af", "loudnorm=I=-20:LRA=11:TP=-2",
            treated_path
        ], check=True)

    def recombine(video_path, treated_audio_path, output_path):
        subprocess.run([
            "ffmpeg", "-y", "-i", video_path, "-i", treated_audio_path,
            "-c:v", codec,
            "-preset", preset,
            "-crf", crf,
            "-c:a", "aac",
            "-b:a", audio_bitrate,
            "-map", "0:v:0", "-map", "1:a:0",
            "-shortest",
            output_path
        ], check=True)

    def process_video(video_path):
        base = os.path.splitext(video_path)[0]
        audio_original = base + "_audio.wav"
        audio_treated = base + "_audio_treated.wav"
        output = base + "_final.mp4"

        print(f"\n🎧 Processing: {os.path.basename(video_path)}")
        extract_audio(video_path, audio_original)
        normalize_audio_ffmpeg(audio_original, audio_treated)
        recombine(video_path, audio_treated, output)
        print(f"✅ Generated: {output}")

    for file in os.listdir(directory):
        if file.lower().endswith(('.mp4', '.mov', '.mkv')):
            path = os.path.join(directory, file)
            try:
                process_video(path)
            except subprocess.CalledProcessError as e:
                print(f"❌ Error processing {file}: {e}")

if __name__ == '__main__':
    main()
