import ollama
import pyttsx3
import whisper
import pyaudio
import wave

def record_audio():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "test.mp3"

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
        input_device_index=2

model = whisper.load_model("base")
result = model.transcribe("./audio/test.mp3")
print(result["text"])

engine = pyttsx3.init()
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_GeorgeM")
engine.setProperty("rate", 150)

user_input = input()
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
