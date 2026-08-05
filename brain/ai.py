# ==========================
# Juno Version 14
# AI Module
# ==========================

import ollama

from system.config import AI_NAME, OWNER_NAME, MODEL_NAME
from brain.personality import SYSTEM_PROMPT
from brain.conversation import add, history


def ask_ai(message):

    add("user", message)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(history())

    try:

        response = ollama.chat(
            model=MODEL_NAME,
            messages=messages
        )

        reply = response["message"]["content"].strip()

        add("assistant", reply)

        return reply

    except Exception as e:

        return f"Sorry {OWNER_NAME}, I couldn't contact the AI model.\n\n{e}"