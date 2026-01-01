import whisper

model = whisper.load_model("base")

result = model.transcribe("audio.wav")

print("Your Speech in Text:")
print(result["text"])
