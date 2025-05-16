# utils.py
import os
from datetime import datetime

def get_today_folder():
    today = datetime.now()
    folder = f"data/{today.year}/{today.month:02d}/{today.day:02d}/"
    os.makedirs(folder, exist_ok=True)
    return folder

def get_next_meeting_id(folder):
    files = [f for f in os.listdir(folder) if f.startswith("meeting_") and f.endswith(".mp4")]
    return len(files) + 1
