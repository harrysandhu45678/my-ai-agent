from brain.memory import remember


def auto_remember(command):
    """
    Automatically remember simple personal facts.
    """

    text = command.strip()
    lower = text.lower()

    # My ... is ...
    if lower.startswith("my ") and " is " in lower:

        index = lower.find(" is ")

        key = text[:index].strip()
        value = text[index + 4:].strip()

        remember(key, value)

        return f"I'll remember that {key} is {value}."

    # I like ...
    if lower.startswith("i like "):

        value = text[7:].strip()

        remember("likes", value)

        return f"I'll remember that you like {value}."

    # I love ...
    if lower.startswith("i love "):

        value = text[7:].strip()

        remember("loves", value)

        return f"I'll remember that you love {value}."

    # I prefer ...
    if lower.startswith("i prefer "):

        value = text[9:].strip()

        remember("prefers", value)

        return f"I'll remember that you prefer {value}."

    return None