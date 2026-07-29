from brain.memory import remember, recall, forget, list_memories


def process_command(command):
    command = command.strip()

    # Remember
    if command.lower().startswith("remember "):

        text = command[9:]

        if " is " not in text:
            return "Please say it like: Remember my favorite color is blue."

        key, value = text.split(" is ", 1)

        remember(key.strip(), value.strip())

        return f"I'll remember that {key.strip()} is {value.strip()}."

    # Recall
    if command.lower().startswith("what is "):

        key = command[8:].strip()

        value = recall(key)

        if value:
            return f"{key} is {value}."

        return f"I don't remember {key}."

    # Forget
    if command.lower().startswith("forget "):

        key = command[7:].strip()

        if forget(key):
            return f"I forgot {key}."

        return f"I don't remember {key}."

    # Show memories
    if command.lower() == "show memories":

        memory = list_memories()

        if not memory:
            return "I don't have any memories yet."

        text = "Here is what I remember:\n"

        for key, value in memory.items():
            text += f"- {key}: {value['value']}\n"

        return text

    return None