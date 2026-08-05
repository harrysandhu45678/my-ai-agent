# ==========================
# Juno Version 14
# Chat Manager
# ==========================

from system.assistant import Assistant
from system.startup import startup

from brain.intents import process_intent


assistant = Assistant()


def reply(text):
    print("Juno:", text)


def start_chat():

    startup()

    while True:

        from voice.manager import (
            get_command,
            enable_voice,
            disable_voice,
            is_voice
        )

        command = get_command()

        if command is None:
            continue

        command = command.strip()

        if command.lower() == "voice":

            enable_voice()

            reply("Voice mode enabled.")

            continue


        if command.lower() == "text":

            disable_voice()

            reply("Text mode enabled.")

            continue

        if command == "":
            continue

        # -------------------------
        # Exit
        # -------------------------

        if command.lower() == "exit":
            reply("Goodbye Harry!")
            break

        # -------------------------
        # Assistant State
        # -------------------------

        if command.lower() == "sleep":
            reply(assistant.sleep())
            continue

        if command.lower() == "wake up":
            reply(assistant.wake())
            continue

        if command.lower() == "status":
            reply(assistant.status())
            continue

        if not assistant.is_awake():
            reply("I'm sleeping. Say wake up.")
            continue

        # -------------------------
        # Intent Engine
        # -------------------------

        response = process_intent(command)

        reply(response)