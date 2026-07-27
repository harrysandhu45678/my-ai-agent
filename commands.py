# ===========================
# Juno Command Handler
# ===========================

from datetime import datetime
from config import AI_NAME


def basic_commands(command):

    text = command.lower().strip()

    # Exit
    if text == "exit":
        return "EXIT"

    # Time
    if text == "time":
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"

    # Date
    if text == "date":
        return f"Today is {datetime.now().strftime('%A, %d %B %Y')}"

    # Greeting
    if text in ["hi", "hello", "hey"]:
        return f"Hello! I'm {AI_NAME}. How can I help you today?"

    # Who are you?
    if text == "who are you":
        return f"I am {AI_NAME}, your personal AI assistant."

    # Thank you
    if text in ["thanks", "thank you"]:
        return "You're welcome!"

    return False