# ===========================
# Juno Command Handler
# ===========================

from config import AI_NAME
from system import get_time, get_date, battery_status, system_info


def basic_commands(command):
    text = command.lower().strip()

    # Exit
    if text == "exit":
        return "EXIT"

    # Greetings
    if text in ("hi", "hello", "hey"):
        return f"Hello! I'm {AI_NAME}. How can I help you?"

    if text == "who are you":
        return f"I am {AI_NAME}, your personal AI assistant."

    if text in ("thanks", "thank you"):
        return "You're welcome!"

    # Time
    if text in ("time", "what time is it", "current time"):
        return f"The current time is {get_time()}."

    # Date
    if text in ("date", "today's date", "what is today's date"):
        return f"Today is {get_date()}."

    # Battery
    if text in ("battery", "battery status"):
        return battery_status()

    # System
    if text in ("system", "system info", "pc info"):
        return system_info()

    return False
