# ==========================
# Juno Version 14
# Desktop Actions
# ==========================

from system.apps import open_app
from system.websites import open_website
from system.folders import open_folder


def execute_action(command):

    text = command.lower().strip()

    if text.startswith("open "):

        target = text.replace("open ", "", 1)

        result = open_app(target)

        if result:
            return result

        result = open_website(target)

        if result:
            return result

        result = open_folder(target)

        if result:
            return result

    return None