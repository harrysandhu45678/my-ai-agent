# ===========================
# Juno AI Module
# ===========================

import ollama
from conversation import get_history

SYSTEM_PROMPT = """
You are Juno, a smart, friendly personal AI assistant.

Rules:
- Be helpful and concise.
- Remember the conversation.
- If the user asks about previous messages, use the conversation history.
- Don't invent personal facts.
- Answer naturally like ChatGPT.
"""

def ask_ai(user_message):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(get_history())

    messages.append({
        "role": "user",
        "content": user_message
    })

    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    return response["message"]["content"]