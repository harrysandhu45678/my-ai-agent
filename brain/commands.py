from brain.memory import remember, recall, forget, all_memory


def process_command(command):

    command = command.strip()

    if command.lower().startswith("remember "):

        text = command[9:]

        if " is " in text:

            key, value = text.split(" is ", 1)

            remember(key.strip(), value.strip())

            return f"I'll remember that {key.strip()} is {value.strip()}."

        return "Say it like: remember favorite color is blue."

    if command.lower().startswith("what is "):

        key = command[8:].strip()

        value = recall(key)

        if value:
            return f"{key} is {value}."

        return "I don't remember."

    if command.lower() == "show memories":

        memory = all_memory()

        if not memory:
            return "Memory is empty."

        text = ""

        for key, value in memory.items():
            text += f"{key} : {value}\n"

        return text

    if command.lower().startswith("forget "):

        key = command[7:]

        if forget(key):
            return f"I forgot {key}."

        return "Nothing to forget."

    return None