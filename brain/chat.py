# ==========================
# Juno Version 14
# Chat Manager
# ==========================

from brain.ai import ask_ai
from brain.commands import process_command

from system.assistant import Assistant
from system.actions import execute_action
from system.startup import startup

assistant = Assistant()


def reply(text):
    print("Juno:", text)


def start_chat():

    startup()

    while True:

        command = input("Harry: ").strip()

        if command == "":
            continue

        # -------------------------
        # Exit
        # -------------------------

        if command.lower() == "exit":

            reply("Goodbye Harry!")

            break

        # -------------------------
        # Assistant
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
        # Desktop Actions
        # -------------------------

        action = execute_action(command)

        if action:

            reply(action)

            continue

        # -------------------------
        # Memory Commands
        # -------------------------

        result = process_command(command)

        if result:

            reply(result)

            continue

        # -------------------------
        # AI
        # -------------------------

        response = ask_ai(command)

        reply(response)