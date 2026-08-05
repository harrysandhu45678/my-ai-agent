# ==========================
# Juno Version 14
# Natural Recall
# ==========================

from brain.memory import recall


def natural_recall(command):

    text = command.lower().strip()

    text = text.replace("?", "")
    text = text.replace(".", "")
    text = text.replace("!", "")

    text = " ".join(text.split())

    # Remove punctuation
    text = text.replace("?", "").replace(".", "").replace("!", "")

    questions = {

        "what's my name": "name",
        "what is my name": "name",

        "what's my favorite color": "favorite_color",
        "what is my favorite color": "favorite_color",

        "what's my favorite food": "favorite_food",
        "what is my favorite food": "favorite_food",

        "what's my favorite movie": "favorite_movie",
        "what is my favorite movie": "favorite_movie",

        "where do i live": "city",

        "what's my hobby": "hobby",
        "what is my hobby": "hobby",

        "what's my birthday": "birthday",
        "what is my birthday": "birthday",

        "where do i study": "university",

        "where do i work": "company"
    }

    if text in questions:

        key = questions[text]

        value = recall(key)

        if value:
            return f"Your {key.replace('_', ' ')} is {value}."

        return "I don't remember that yet."

    return None