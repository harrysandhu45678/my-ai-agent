import json
import os
import subprocess

APP_FILE = "data/apps.json"


def load_apps():
    if not os.path.exists(APP_FILE):
        return {}

    try:
        with open(APP_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_apps(apps):
    with open(APP_FILE, "w") as f:
        json.dump(apps, f, indent=4)


def learn_app(name, path):
    apps = load_apps()

    apps[name.lower()] = path

    save_apps(apps)

    return f"I've learned how to open {name}."


def open_learned_app(name):
    apps = load_apps()

    path = apps.get(name.lower())

    if not path:
        return None

    try:
        subprocess.Popen(path)
        return f"Opening {name}."

    except Exception:
        return f"I know {name}, but I couldn't open it."