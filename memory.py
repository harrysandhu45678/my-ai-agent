import json
import os
import re
from config import MEMORY_FILE, OWNER_NAME


def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


memory = load_memory()


# -------------------------
# Manual memory
# -------------------------

def remember(command):

    if not command.lower().startswith("remember "):
        return False

    fact = command[9:]

    if " is " not in fact:
        return "Please say:\nremember my pet is Rocky"

    key, value = fact.split(" is ", 1)

    key = key.strip().lower()
    value = value.strip()

    memory[key] = value
    save_memory(memory)

    return "I'll remember that."


# -------------------------
# Automatic memory
# -------------------------

AUTO_PATTERNS = [
    (r"my (.+?) is (.+)", "my {}"),
    (r"i live in (.+)", "my city"),
    (r"i am from (.+)", "my hometown"),
    (r"my name is (.+)", "name"),
    (r"my birthday is (.+)", "my birthday"),
]


def auto_remember(command):

    text = command.strip()

    for pattern, key_template in AUTO_PATTERNS:

        match = re.fullmatch(pattern, text, re.IGNORECASE)

        if not match:
            continue

        groups = match.groups()

        if "{}" in key_template:

            key = key_template.format(groups[0].strip().lower())
            value = groups[1].strip()

        else:

            key = key_template
            value = groups[0].strip()

        old = memory.get(key)

        if old == value:
            return None

        memory[key] = value
        save_memory(memory)

        return f"I'll remember that ({key}: {value})."

    return None


# -------------------------
# Show memory
# -------------------------

def show_memory(command):

    if command.lower() != "what do you remember":
        return False

    if not memory:
        return "I don't remember anything yet."

    text = "Here's everything I know:\n\n"

    for key, value in sorted(memory.items()):
        text += f"• {key.title()} : {value}\n"

    return text


# -------------------------
# Answer memory questions
# -------------------------

def answer_memory(command):

    text = command.lower().strip().rstrip("?")

    if text in ["tell me about myself", "what do you know about me"]:

        if not memory:
            return "I don't know much about you yet."

        result = "Here's what I know about you:\n\n"

        for key, value in sorted(memory.items()):
            result += f"• {key.title()} : {value}\n"

        return result

    if text == "who am i":

        if "name" in memory:
            return f"You are {memory['name']}."

        return f"You are {OWNER_NAME}."

    if text.startswith("what is my "):

        key = "my " + text.replace("what is my ", "")

        if key in memory:
            return memory[key]

        return "I don't know that yet."

    if text.startswith("when is my "):

        key = "my " + text.replace("when is my ", "")

        if key in memory:
            return memory[key]

        return "I don't know that yet."

    if text == "where do i live":

        if "my city" in memory:
            return memory["my city"]

        return "I don't know where you live."

    if text.startswith("which ") and text.endswith(" do i have"):

        thing = text.replace("which ", "").replace(" do i have", "")
        key = "my " + thing

        if key in memory:
            return memory[key]

        return "I don't know that yet."

    return False