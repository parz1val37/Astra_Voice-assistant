# Uncomplete! leaving this project for sometime..
import speech_recognition as sr
import webbrowser
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 200)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")


if __name__ == "__main__":
    speak("Initializing Astra....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            print("Recognizing...")

            word = r.recognize_google(audio)
            print(f"You said: {word}")
            if word.lower() == "astra":
                # speak("How can I assist you")
                with sr.Microphone() as source:
                    print("Astra is active...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=2)
                    command = r.recognize_google(audio)

                    processcommand(command)
        

        except Exception as e:
            print(f"Error: {e}")
