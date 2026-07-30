import os
import webbrowser


def open_website(url):
    webbrowser.open(url)
    return f"Opening {url}."


def open_vscode():
    os.system("code")
    return "Opening Visual Studio Code."


def open_notepad():
    os.system("notepad")
    return "Opening Notepad."


def open_calculator():
    os.system("calc")
    return "Opening Calculator."