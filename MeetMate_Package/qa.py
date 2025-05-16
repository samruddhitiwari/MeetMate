# qa.py
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def ask_question(transcript_path, question):
    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript = f.read()

    prompt = f"The following is a meeting transcript:\n{transcript}\n\nQuestion: {question}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message["content"]
