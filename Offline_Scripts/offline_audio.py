# Use a pipeline as a high-level helper
from transformers import pipeline

model_path = '../models/models--openai--whisper-medium/snapshots/abdf7c39ab9d0397620ccaea8974cc764cd0953e'
audio_path = "./audioDir/harvard.wav"
pipe = pipeline("automatic-speech-recognition", model=model_path)
out = pipe(audio_path)
print(out)