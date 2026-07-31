from brain.memory import remember, recall, forget, list_memories
from brain.memory_manager import auto_remember

from actions.system_actions import open_app, open_website
from actions.app_manager import learn_app


def process_command(command):

    command = command.strip()
    lower = command.lower()

    # --------------------------
    # Automatic Memory
    # --------------------------

    auto = auto_remember(command)

    if auto:
        return auto

    # --------------------------
    # Learn Application
    # --------------------------

    if lower.startswith("learn app "):

        text = command[10:].strip()

        parts = text.split(" ", 1)

        if len(parts) != 2:
            return "Use: learn app <name> <path>"

        app_name = parts[0]
        app_path = parts[1]

        return learn_app(app_name, app_path)

    # --------------------------
    # Desktop Actions
    # --------------------------

    if lower.startswith("open "):

        item = command[5:].strip()

        # Websites
        if item.lower() in [
            "google",
            "youtube",
            "github",
            "chatgpt",
        ]:
            return open_website(item)

        # Applications
        return open_app(item)

    # --------------------------
    # Manual Remember
    # --------------------------

    if lower.startswith("remember "):

        text = command[9:]

        if " is " not in text:
            return "Please say it like: Remember my favorite color is blue."

        key, value = text.split(" is ", 1)

        remember(key.strip(), value.strip())

        return f"I'll remember that {key.strip()} is {value.strip()}."

    # --------------------------
    # Recall
    # --------------------------

    key = None

    if lower.startswith("what is "):
        key = command[8:].strip()

    elif lower.startswith("what's "):
        key = command[7:].strip()

    elif lower.startswith("do you remember "):
        key = command[16:].strip()

    elif lower.startswith("can you tell me "):
        key = command[16:].strip()

    if key:

        key = key.replace("?", "").strip()

        value = recall(key)

        if value:
            return f"{key} is {value}."

        return f"I don't remember {key}."

    # --------------------------
    # Forget
    # --------------------------

    if lower.startswith("forget "):

        key = command[7:].strip()

        if forget(key):
            return f"I forgot {key}."

        return f"I don't remember {key}."

    # --------------------------
    # Show Memories
    # --------------------------

    if lower == "show memories":

        memory = list_memories()

        if not memory:
            return "I don't have any memories yet."

        text = "Here is what I remember:\n"

        for key, value in memory.items():
            text += f"- {key}: {value['value']}\n"

        return text

    return None