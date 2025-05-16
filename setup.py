from setuptools import setup, find_packages

setup(
    name="meeting-assistant",
    version="0.1.0",
    author="Samruddhi Tiwari",
    description="AI-based meeting assistant for recording, transcribing, summarizing and querying meetings.",
    packages=find_packages(),
    install_requires=[
        "openai",
        "whisper",
        "pyaudio",
        "ffmpeg-python",
        "tk",  # optional, may already be part of stdlib
        "transformers",
        "torch",
    ],
    entry_points={
        "console_scripts": [
            "meeting-assistant=meeting_assistant.gui:main"
        ]
    },
    python_requires='>=3.8',
)
