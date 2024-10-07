from openai import OpenAI
from docx import Document
client = OpenAI(api_key="...")
with open("/content/Japanese Listening Practice.mp3", "rb") as audio_file:
    transcript_es = client.audio.transcriptions.create(
        file = audio_file,
        model = "whisper-1",
        response_format="text",
        language="ja" #select language
    )
print(transcript_es)
print("translation:")


with open("/content/Japanese Listening Practice.mp3", "rb") as audio_file:
    translation = client.audio.translations.create(
        file = audio_file,
        model = "whisper-1",
        response_format="text"
    )
print(translation)
