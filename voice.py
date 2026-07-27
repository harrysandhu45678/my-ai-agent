import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Voice settings
engine.setProperty("rate", 170)      # Speaking speed
engine.setProperty("volume", 1.0)    # Volume (0.0 - 1.0)

voices = engine.getProperty("voices")
if voices:
    engine.setProperty("voice", voices[0].id)


def speak(text):
    """Speak text aloud."""
    print(f"Juno: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen through the microphone and convert speech to text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

            print("🧠 Recognizing...")

            command = recognizer.recognize_google(audio)

            print(f"Harry: {command}")

            return command

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return None

        except sr.RequestError:
            print("Speech Recognition service is unavailable.")
            return None