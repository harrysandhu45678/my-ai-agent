# brain/conversation.py

MAX_HISTORY = 20

conversation = []


def add_message(role, content):
    """
    Add a message to the conversation history.
    role: "user" or "assistant"
    """

    conversation.append({
        "role": role,
        "content": content
    })

    if len(conversation) > MAX_HISTORY:
        conversation.pop(0)


def get_history():
    """
    Return conversation history.
    """

    return conversation.copy()


def clear_history():
    """
    Clear conversation.
    """

    conversation.clear()