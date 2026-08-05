import subprocess


APPS = {
    "calculator": "calc",
    "notepad": "notepad",
    "paint": "mspaint",
    "command prompt": "cmd",
    "file explorer": "explorer",
    "explorer": "explorer",
}


def open_app(app):

    app = app.lower()

    if app in APPS:
        subprocess.Popen(APPS[app], shell=True)
        return f"Opening {app.title()}."

    if app in ["vscode", "vs code"]:
        subprocess.Popen("code", shell=True)
        return "Opening VS Code."

    if app == "chrome":
        subprocess.Popen("start chrome", shell=True)
        return "Opening Chrome."

    return None