# transcribe.py
import whisper

def transcribe_audio(file_path, transcript_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
