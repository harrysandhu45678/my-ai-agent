import json
import os
from config import MEMORY_FILE


def load_memory():
    """Load memory from memory.json"""
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}


def save_memory(memory):
    """Save memory to memory.json"""
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


memory = load_memory()


def remember(command):
    """
    Example:
    remember my pet is Rocky
    remember my city is Kurukshetra
    """

    if not command.lower().startswith("remember "):
        return False

    fact = command[9:]

    if " is " not in fact:
        return "Please say it like:\nremember my pet is Rocky"

    key, value = fact.split(" is ", 1)

    memory[key.strip().lower()] = value.strip()

    save_memory(memory)

    return "I'll remember that."


def show_memory(command):

    if command.lower() != "what do you remember":
        return False

    if not memory:
        return "I don't remember anything yet."

    text = "Here's everything I know:\n\n"

    for key, value in memory.items():
        text += f"• {key.title()} : {value}\n"

    return text


def answer_memory(command):

    text = command.lower().strip().rstrip("?")

    if text in ["tell me about myself", "what do you know about me"]:

        if not memory:
            return "I don't know much about you yet."

        result = "Here's what I know about you:\n\n"

        for key, value in memory.items():
            result += f"• {key.title()} : {value}\n"

        return result

    if text == "who am i":
        return "You are Harry."

    if text == "where do i live":

        if "my city" in memory:
            return memory["my city"]

        return "I don't know where you live yet."

    if text == "when is my birthday":

        if "my birthday" in memory:
            return memory["my birthday"]

        return "I don't know your birthday yet."

    if text == "what is my pet":

        if "my pet" in memory:
            return memory["my pet"]

        return "I don't know your pet yet."

    if text == "which bike do i have":

        if "my bike" in memory:
            return memory["my bike"]

        return "I don't know your bike yet."

    if text.startswith("what is my "):

        key = "my " + text.replace("what is my ", "")

        if key in memory:
            return memory[key]

        return "I don't know that yet."

    return False