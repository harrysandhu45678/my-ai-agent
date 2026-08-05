# ==========================
# Juno Version 14
# Desktop Actions
# ==========================

import subprocess
import webbrowser


def execute_action(command):

    cmd = command.lower().strip()

    # -------------------------
    # Applications
    # -------------------------

    apps = {
        "open calculator": "calc",
        "open notepad": "notepad",
        "open paint": "mspaint",
        "open command prompt": "cmd",
        "open file explorer": "explorer",
        "open explorer": "explorer",
    }

    if cmd in apps:
        subprocess.Popen(apps[cmd], shell=True)
        return f"Opening {cmd.replace('open ', '').title()}."

    # VS Code
    if cmd in ["open vscode", "open vs code"]:
        subprocess.Popen("code", shell=True)
        return "Opening VS Code."

    # Chrome
    if cmd == "open chrome":
        subprocess.Popen("start chrome", shell=True)
        return "Opening Chrome."

    # -------------------------
    # Websites
    # -------------------------

    websites = {
        "open google": "https://google.com",
        "open youtube": "https://youtube.com",
        "open github": "https://github.com",
        "open gmail": "https://mail.google.com",
    }

    if cmd in websites:
        webbrowser.open(websites[cmd])
        return f"Opening {cmd.replace('open ', '').title()}."

    return None