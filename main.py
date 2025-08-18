import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 200)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Astra....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=4, phrase_time_limit=3)
            print("Recognizing...")

            word = r.recognize_google(audio)
            if word.lower() == "hello":
                speak("How can I assist you?")
                # with sr.Microphone() as source:
                #     print("Listening for command...")
                #     audio = r.listen(source, timeout=2, phrase_time_limit=1)


        except Exception as e:
            print(f"Error: {e}")
            continue