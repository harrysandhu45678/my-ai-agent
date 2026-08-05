# ==========================
# Conversation Manager
# ==========================

conversation = []

from system.config import MAX_HISTORY


def add(role, content):

    conversation.append({
        "role": role,
        "content": content
    })

    if len(conversation) > MAX_HISTORY:
        conversation.pop(0)


def history():
    return conversation.copy()


def clear():
    conversation.clear()