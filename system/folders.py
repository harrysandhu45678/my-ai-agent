import os
import subprocess


FOLDERS = {
    "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
    "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "documents": os.path.join(os.path.expanduser("~"), "Documents"),
    "pictures": os.path.join(os.path.expanduser("~"), "Pictures"),
}


def open_folder(folder):

    folder = folder.lower()

    if folder in FOLDERS:
        subprocess.Popen(f'explorer "{FOLDERS[folder]}"')
        return f"Opening {folder.title()}."

    return None