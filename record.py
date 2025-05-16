# record.py
import subprocess

def record_screen(output_file, duration=600):
    command = [
        'ffmpeg',
        '-y',
        '-f', 'gdigrab',
        '-framerate', '30',
        '-i', 'desktop',
        '-f', 'dshow',
        '-i', 'audio="virtual-audio-capturer"',
        '-t', str(duration),
        '-vcodec', 'libx264',
        output_file
    ]
    print("Recording started...")
    subprocess.run(command)
    print("Recording finished.")
