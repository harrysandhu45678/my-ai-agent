# ==========================
# Juno Version 15
# Natural Action Parser
# ==========================

ACTION_WORDS = [
    "open",
    "launch",
    "start",
    "run",
]


def parse_action(command):

    text = command.lower().strip()

    # Remove punctuation
    for ch in ["?", ".", "!", ","]:
        text = text.replace(ch, "")

    words = text.split()

    for action in ACTION_WORDS:

        if action in words:

            index = words.index(action)

            if index + 1 < len(words):

                target = " ".join(words[index + 1:])

                # Remove filler words
                fillers = [
                    "the",
                    "my",
                    "a",
                    "an",
                    "please",
                ]

                target = " ".join(
                    word for word in target.split()
                    if word not in fillers
                )

                return {
                    "intent": "action",
                    "text": f"open {target}"
                }

    # Natural recall
    if text.startswith(("what", "where", "who", "when")):
        return {
            "intent": "recall",
            "text": text
        }

    # Automatic memory
    if text.startswith(("my", "i am", "i'm", "i live")):
        return {
            "intent": "memory",
            "text": text
        }

    # Default to AI
    return {
        "intent": "ai",
        "text": text
    }