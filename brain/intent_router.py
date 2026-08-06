# ==========================
# Juno Version 15
# Intent Router
# ==========================

from brain.auto_memory import auto_remember
from brain.recall import natural_recall
from brain.commands import process_command
from brain.ai import ask_ai

from system.actions import execute_action


def process_intent(intent):

    intent_type = intent["intent"]

    text = intent["text"]

    if intent_type == "action":

        result = execute_action(text)

        if result:
            return result

    if intent_type == "memory":

        result = auto_remember(text)

        if result:
            return result

    if intent_type == "recall":

        result = natural_recall(text)

        if result:
            return result

    result = process_command(text)

    if result:
        return result

    return ask_ai(text)