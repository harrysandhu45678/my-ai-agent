import os
import subprocess
import webbrowser
from actions.app_manager import open_learned_app

# -------------------------
# Websites
# -------------------------

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "chatgpt": "https://chat.openai.com",
}


# -------------------------
# Applications
# -------------------------

APPLICATIONS = {
    "vscode": "code",
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "chrome": "start chrome",
}


def open_website(name):

    url = WEBSITES.get(name.lower())

    if not url:
        return f"I don't know the website '{name}'."

    webbrowser.open(url)

    return f"Opening {name}."


def open_app(name):

    name = name.lower()

    # Open CMD in a new window
    if name == "cmd":
        subprocess.Popen("cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)
        return "Opening Command Prompt."

        # Check learned applications first
    learned = open_learned_app(name)

    if learned:
        return learned

    app = APPLICATIONS.get(name)

    if not app:
        return f"I don't know how to open '{name}'."

    os.system(app)

    return f"Opening {name}."