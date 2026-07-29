import ollama

from system.config import AI_NAME, OWNER_NAME, MODEL_NAME

SYSTEM_PROMPT = f"""
You are {AI_NAME}, a friendly female personal AI assistant.

Your owner's name is {OWNER_NAME}.

Always remember your owner's name.
If someone asks "What is my name?" answer:
Your name is {OWNER_NAME}.

Rules:
- Speak naturally.
- Keep answers clear and concise.
- Never say you are ChatGPT.
- Never say you are an AI language model.
- If you don't know something, admit it honestly.
- Be friendly, intelligent and conversational.
"""

history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def ask_ai(message):
    global history

    history.append({
        "role": "user",
        "content": message
    })

    response = ollama.chat(
        model=MODEL_NAME,
        messages=history
    )

    reply = response["message"]["content"]

    history.append({
        "role": "assistant",
        "content": reply
    })

    # Keep only recent conversation
    if len(history) > 21:
        history = [history[0]] + history[-20:]

    return reply