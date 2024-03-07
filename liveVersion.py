import ollama
import pyttsx3
import whisper
import pyaudio
import wave

model = whisper.load_model("base")
result = model.transcribe("./audio/test.mp3")
print(result["text"])

engine = pyttsx3.init()
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_GeorgeM")
engine.setProperty("rate", 150)

user_input = input()
user_input = "Who are you?"
print(user_input)
stream = ollama.chat(
    model='bagley',
    messages=[{'role': 'user', 'content': user_input}],
    stream=True,
)

generated_text = ""

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
  generated_text += chunk['message']['content']

engine.say(generated_text)
engine.runAndWait()
engine.stop()
