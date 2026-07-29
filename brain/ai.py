import ollama

from system.config import MODEL_NAME
from brain.conversation import add_message, get_history


SYSTEM_PROMPT = """
You are Juno, a friendly female personal AI assistant.

You are helpful, conversational and concise.

Never claim to remember something unless it appears in the conversation or long-term memory.

Respond naturally.
"""


def ask_ai(message):

    # Save user's message
    add_message("user", message)

    # Build messages for Ollama
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(get_history())

    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages
    )

    reply = response["message"]["content"]

    # Save AI reply
    add_message("assistant", reply)

    return reply