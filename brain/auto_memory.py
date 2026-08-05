# ==========================
# Juno Version 14
# Automatic Memory
# ==========================

from brain.memory import remember
from brain.memory_schema import MEMORY_PATTERNS


def auto_remember(command):

    text = command.lower().strip()

    for pattern, key in MEMORY_PATTERNS.items():

        if text.startswith(pattern):

            value = command[len(pattern):].strip()

            remember(key, value)

            return "I'll remember that."

    return None