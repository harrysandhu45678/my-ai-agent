# ==========================
# Juno Version 14
# Natural Action Parser
# ==========================

ACTION_PATTERNS = [

    "open",
    "launch",
    "start",
    "run",

]


def parse_action(command):

    text = command.lower()

    for action in ACTION_PATTERNS:

        if action in text:

            words = text.split()

            if action in words:

                index = words.index(action)

                if index + 1 < len(words):

                    target = " ".join(words[index + 1:])

                    # Remove common filler words
                    fillers = [
                        "the",
                        "my",
                        "a",
                        "an",
                        "please",
                    ]

                    target_words = [
                        w for w in target.split()
                        if w not in fillers
                    ]

                    return "open " + " ".join(target_words)

    return command