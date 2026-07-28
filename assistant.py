from voice import speak, voice_enabled


class Assistant:
    def __init__(self):
        self.awake = True

    # -------------------------
    # Startup
    # -------------------------
    def greet(self):
        speak("Hello Harry. Juno is ready.")

    # -------------------------
    # Sleep / Wake
    # -------------------------
    def sleep(self):
        self.awake = False
        speak("Going to sleep.")

    def wake(self):
        self.awake = True
        speak("I'm awake.")

    # -------------------------
    # Status
    # -------------------------
    def status(self):
        if not self.awake:
            speak("I am currently sleeping.")
            return

        if voice_enabled():
            speak("Voice mode is active.")
        else:
            speak("Text mode is active.")

    # -------------------------
    # State
    # -------------------------
    def is_awake(self):
        return self.awake
