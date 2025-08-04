import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Try setting female voice (use voices[1] if available)
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    text = input("Say something (or 'exit' to quit): ")
    if text.lower() == 'exit':
        break
    speak(text)