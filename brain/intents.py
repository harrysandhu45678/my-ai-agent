# ==========================
# Juno Version 14
# Intent Engine
# ==========================

from brain.action_parser import parse_action
from brain.recall import natural_recall
from brain.auto_memory import auto_remember
from brain.commands import process_command
from brain.ai import ask_ai
from system.actions import execute_action


def process_intent(command):

    command = command.strip()
    command = parse_action(command)

    if not command:
        return "Please say something."

    # -------------------------
    # Desktop Actions
    # -------------------------

    action = execute_action(command)

    if action:
        return action

    # -------------------------
    # Automatic Memory
    # -------------------------

    auto = auto_remember(command)

    if auto:
        return auto

    # -------------------------
    # Natural Recall
    # -------------------------

    recall = natural_recall(command)

    if recall:
        return recall

    # -------------------------
    # Manual Memory Commands
    # -------------------------

    memory = process_command(command)

    if memory:
        return memory

    # -------------------------
    # AI
    # -------------------------

    return ask_ai(command)