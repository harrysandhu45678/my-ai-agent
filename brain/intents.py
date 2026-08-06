# ==========================
# Juno Version 14
# Intent Engine
# ==========================

from brain.action_parser import parse_action
from brain.intent_router import process_intent


def handle(command):

    intent = parse_action(command)

    return process_intent(intent)