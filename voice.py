import speech_recognition as sr
import pyttsx3
import time

# ----------------------------
# Initialize TTS
# ----------------------------
engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

# ----------------------------
# Select Female Voice
# ----------------------------
voices = engine.getProperty("voices")

female_found = False

for voice in voices:
    name = voice.name.lower()

    if (
        "zira" in name
        or "aria" in name
        or "female" in name
        or "hazel" in name
        or "eva" in name
        or "susan" in name
    ):
        engine.setProperty("voice", voice.id)
        female_found = True
        print(f"Female voice selected: {voice.name}")
        break

if not female_found:
    print("Female voice not found. Using default voice.")
    if voices:
        engine.setProperty("voice", voices[0].id)


# ----------------------------
# Speak
# ----------------------------
def speak(text):
    print(f"Juno: {text}")
    engine.say(text)
    engine.runAndWait()


# ----------------------------
# Listen
# ----------------------------
def listen():

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8

    with sr.Microphone() as source:

        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.8)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            print("🧠 Recognizing...")

            command = recognizer.recognize_google(audio)

            command = command.strip()

            print(f"Harry: {command}")

            return command

        except sr.WaitTimeoutError:
            return None

        except sr.UnknownValueError:
            print("I couldn't understand.")
            return None

        except sr.RequestError:
            print("Internet connection required.")
            return None

        except OSError:
            print("Microphone not available.")
            return None

        except Exception as e:
            print(f"Voice Error: {e}")
            time.sleep(1)
            return None