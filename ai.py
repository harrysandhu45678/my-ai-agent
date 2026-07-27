# ===========================
# Juno AI Module
# ===========================

import ollama
from config import AI_NAME, OWNER_NAME, MODEL_NAME


SYSTEM_PROMPT = f"""
You are {AI_NAME}.

You are a friendly, intelligent and helpful AI assistant.

The user's name is {OWNER_NAME}.

Always answer politely.

Keep answers clear.

If someone asks about something stored in memory,
the main program will already answer it before it reaches you.

Otherwise help the user normally.
"""


def ask_llama(prompt):

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]