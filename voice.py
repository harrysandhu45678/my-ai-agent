import speech_recognition as sr
import time
from online_voice import speak_online

VOICE_ENABLED = False


def enable_voice():
    global VOICE_ENABLED
    VOICE_ENABLED = True


def disable_voice():
    global VOICE_ENABLED
    VOICE_ENABLED = False


def voice_enabled():
    return VOICE_ENABLED


def speak(text):
    print(f"Juno: {text}")

    if not VOICE_ENABLED:
        return

    try:
        speak_online(str(text))
    except Exception as e:
        print("Online Voice Error:", e)


def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)

            print("\n🎤 Listening...")

            audio = r.listen(
                source,
                timeout=10,
                phrase_time_limit=15
            )

        print("🧠 Recognizing...")

        text = r.recognize_google(audio).strip()

        print(f"Harry: {text}")

        return text

    except sr.WaitTimeoutError:
        return None

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
        return None

    except sr.RequestError:
        speak("Internet connection required.")
        return None

    except OSError:
        speak("Microphone not detected.")
        return None

    except Exception as e:
        print("Voice Error:", e)
        time.sleep(1)
        return None