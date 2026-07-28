import speech_recognition as sr
import pyttsx3
import time

VOICE_ENABLED = False

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")

female_found = False

for v in voices:
    n = v.name.lower()

    if any(x in n for x in ["zira", "aria", "female", "hazel", "eva", "susan"]):
        engine.setProperty("voice", v.id)
        female_found = True
        break

if not female_found:
    if voices:
        engine.setProperty("voice", voices[0].id)

def enable_voice():
    global VOICE_ENABLED
    VOICE_ENABLED = True

def disable_voice():
    global VOICE_ENABLED
    VOICE_ENABLED = False

def voice_enabled():
    return VOICE_ENABLED

def speak(text):
    global engine

    print(f"Juno: {text}")

    if not VOICE_ENABLED:
        return

    try:
        engine.stop()          # Clear anything queued
        engine.say(str(text))
        engine.runAndWait()
    except Exception as e:
        print("Speech Error:", e)

        # Recreate the engine if it gets stuck
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", 170)
            engine.setProperty("volume", 1.0)
            engine.say(str(text))
            engine.runAndWait()
        except Exception as e2:
            print("Speech Restart Error:", e2)

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.8

    try:
        with sr.Microphone() as source:
            print("\\n🎤 Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=8)

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
