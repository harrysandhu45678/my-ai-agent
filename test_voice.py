from voice.voice import *

enable_voice()

while True:

    speak("Say something.")

    text = listen()

    if text:

        speak("You said " + text)

        if text == "exit":
            break