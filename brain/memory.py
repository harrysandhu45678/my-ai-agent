import json
import os

MEMORY_FILE = "data/memory.json"


def load():

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save(memory):

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember(key, value):

    memory = load()

    memory[key.lower()] = value

    save(memory)


def recall(key):

    return load().get(key.lower())


def forget(key):

    memory = load()

    if key.lower() in memory:
        del memory[key.lower()]
        save(memory)
        return True

    return False


def all_memory():

    return load()