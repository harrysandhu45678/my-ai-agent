import time
import pyttsx3
import speech_recognition as sr

_engine = pyttsx3.init()

_voice_enabled = False

# ----------------------------
# Select Voice
# ----------------------------
voices = _engine.getProperty("voices")

for voice in voices:
    # Try to select a female Microsoft voice
    if "zira" in voice.name.lower() or "female" in voice.name.lower():
        _engine.setProperty("voice", voice.id)
        break

_engine.setProperty("rate", 180)
_engine.setProperty("volume", 1.0)


# ----------------------------
# Voice Mode
# ----------------------------
def enable_voice():
    global _voice_enabled
    _voice_enabled = True


def disable_voice():
    global _voice_enabled
    _voice_enabled = False


def voice_enabled():
    return _voice_enabled


# ----------------------------
# Speak
# ----------------------------
def speak(text):
    print("Juno:", text)

    if _voice_enabled:
        time.sleep(0.3)   # Give microphone time to release
        _engine.say(text)
        _engine.runAndWait()


# ----------------------------
# Listen
# ----------------------------
def listen():

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8

    with sr.Microphone() as source:

        print("Listening...")

        # Give Juno 2 seconds to learn room noise
        recognizer.adjust_for_ambient_noise(source, duration=2)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            text = recognizer.recognize_google(audio)

            print("Harry:", text)

            return text.lower()

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None

        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return None

        except sr.RequestError:
            print("Speech service unavailable.")
            return None

        except Exception as e:
            print(e)
            return None