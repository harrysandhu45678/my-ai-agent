import speech_recognition as sr


recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

            text = recognizer.recognize_google(audio)

            print("Harry:", text)

            return text

        except sr.UnknownValueError:

            print("Juno: I didn't catch that.")

            return None

        except sr.WaitTimeoutError:

            return None

        except Exception as e:

            print(e)

            return None