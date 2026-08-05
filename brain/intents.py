# ==========================
# Juno Version 14
# Intent Engine
# ==========================

from brain.commands import process_command
from brain.ai import ask_ai
from system.actions import execute_action


def process_intent(command):

    command = command.strip()

    if not command:
        return "Please say something."

    # -------------------------
    # Desktop Actions
    # -------------------------

    action = execute_action(command)

    if action:
        return action

    # -------------------------
    # Memory Commands
    # -------------------------

    memory = process_command(command)

    if memory:
        return memory

    # -------------------------
    # AI
    # -------------------------

    return ask_ai(command)