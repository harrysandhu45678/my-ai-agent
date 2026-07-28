# ===========================
# Juno AI Module
# ===========================

import ollama
from config import AI_NAME, OWNER_NAME, MODEL_NAME

SYSTEM_PROMPT = f"""
You are {AI_NAME}, a friendly female personal AI assistant.
Your owner's name is {OWNER_NAME}.

Rules:
- Speak naturally and briefly.
- Never say you are ChatGPT or an AI language model.
- If you do not know something, say so honestly.
- Be helpful, respectful and conversational.
"""

_history = [{"role": "system", "content": SYSTEM_PROMPT}]

def ask_ai(message: str) -> str:
    global _history

    _history.append({"role": "user", "content": message})

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=_history
        )

        reply = response["message"]["content"].strip()

        _history.append({"role": "assistant", "content": reply})

        # keep recent conversation only
        if len(_history) > 21:
            _history = [_history[0]] + _history[-20:]

        return reply

    except Exception as e:
        return f"Sorry {OWNER_NAME}, I couldn't contact the AI model. Error: {e}"
