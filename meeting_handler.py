# meeting_handler.py
from utils import get_today_folder, get_next_meeting_id
from record import record_screen
from transcribe import transcribe_audio
from summarize import summarize_text

def handle_meeting(link):
    folder = get_today_folder()
    meeting_id = get_next_meeting_id(folder)

    video_path = f"{folder}/meeting_{meeting_id}.mp4"
    transcript_path = f"{folder}/transcript_{meeting_id}.txt"
    summary_path = f"{folder}/summary_{meeting_id}.txt"

    # Step 1: Record the screen (e.g., 10 minutes)
    record_screen(video_path, duration=600)

    # Step 2: Transcribe
    transcribe_audio(video_path, transcript_path)

    # Step 3: Summarize
    summarize_text(transcript_path, summary_path)
