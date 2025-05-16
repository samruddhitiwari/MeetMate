# summarize.py
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def summarize_text(input_path, summary_path):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize the following meeting transcript:\n\n{text}"}],
        temperature=0.5,
    )

    summary = response.choices[0].message["content"]

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)
