import json
import os

MEMORY_FILE = "data/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def remember(key, value):
    memory = load_memory()

    memory[key.lower()] = {
        "value": value
    }

    save_memory(memory)


def recall(key):
    memory = load_memory()

    item = memory.get(key.lower())

    if item:
        return item["value"]

    return None


def forget(key):
    memory = load_memory()

    if key.lower() in memory:
        del memory[key.lower()]
        save_memory(memory)
        return True

    return False


def list_memories():
    return load_memory()