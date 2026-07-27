# ===========================
# Juno Main Program
# ===========================

from config import AI_NAME, OWNER_NAME
from ai import ask_llama
from memory import remember, show_memory, answer_memory
from commands import basic_commands

print("=" * 50)
print(f"🤖 Welcome to {AI_NAME}")
print("=" * 50)
print(f"Hello {OWNER_NAME}!")
print("Type 'exit' anytime to close Juno.")
print()

while True:

    command = input(f"{OWNER_NAME}: ").strip()

    if command == "":
        continue

    # -----------------------
    # Basic Commands
    # -----------------------

    result = basic_commands(command)

    if result == "EXIT":
        print(f"{AI_NAME}: Goodbye {OWNER_NAME}! 👋")
        break

    if result:
        print(f"{AI_NAME}: {result}")
        continue

    # -----------------------
    # Memory Commands
    # -----------------------

    result = remember(command)

    if result:
        print(f"{AI_NAME}: {result}")
        continue

    result = show_memory(command)

    if result:
        print(f"{AI_NAME}:")
        print(result)
        continue

    result = answer_memory(command)

    if result:
        print(f"{AI_NAME}: {result}")
        continue

    # -----------------------
    # AI Chat
    # -----------------------

    try:
        reply = ask_llama(command)
        print(f"{AI_NAME}: {reply}")

    except Exception as e:
        print(f"{AI_NAME}: Error talking to Ollama.")
        print(e)