from system.assistant import Assistant
from brain.ai import ask_ai
from brain.commands import process_command

from voice.voice import (
    enable_voice,
    disable_voice,
    voice_enabled,
    speak,
    listen,
)


assistant = Assistant()


def reply(text):
    if voice_enabled():
        speak(text)
    else:
        print("Juno:", text)


def start_chat():

    print("=================================")
    print("        Juno Version 12")
    print("=================================\n")

    mode = "text"

    while True:

        # --------------------
        # TEXT MODE
        # --------------------
        if mode == "text":

            command = input("Harry: ").strip()

            if command.lower() == "voice":
                mode = "voice"
                enable_voice()
                speak("Voice mode activated.")
                continue

        # --------------------
        # VOICE MODE
        # --------------------
        else:

            command = listen()

            if command is None:
                continue

            if command.lower() == "text mode":
                disable_voice()
                mode = "text"
                print("Juno: Switched to text mode.")
                continue

        command = command.strip()

        # --------------------
        # EXIT
        # --------------------
        if command.lower() == "exit":

            reply("Goodbye Harry!")

            break

        # --------------------
        # Assistant commands
        # --------------------
        if command.lower() == "sleep":
            assistant.sleep()
            continue

        if command.lower() == "wake up":
            assistant.wake()
            continue

        if command.lower() == "status":
            assistant.status()
            continue

        if not assistant.is_awake():

            reply("I'm sleeping. Say wake up.")

            continue

        # --------------------
        # Memory Commands
        # --------------------
        result = process_command(command)

        if result:
            reply(result)
            continue

                # --------------------
        # AI
        # --------------------

        response = ask_ai(command)

        reply(response)