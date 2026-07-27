# ===========================
# Juno Main Program
# ===========================

from config import AI_NAME, OWNER_NAME
from ai import ask_ai
from memory import (
    remember,
    auto_remember,
    answer_memory,
    show_memory
)
from conversation import (
    add_message,
    clear_history
)

print(f"{AI_NAME}: Hello {OWNER_NAME}! 👋")
print("Type 'exit' to quit.")
print("Type 'clear chat' to clear conversation.\n")

while True:
    command = input(f"{OWNER_NAME}: ").strip()

    if not command:
        continue

    if command.lower() == "exit":
        print(f"{AI_NAME}: Goodbye {OWNER_NAME}! 👋")
        break

    if command.lower() == "clear chat":
        clear_history()
        print(f"{AI_NAME}: Conversation cleared.")
        continue

    # Long-term memory
    if remember(command):
        continue

    result = auto_remember(command)
    if result:
        print(f"{AI_NAME}: {result}")
    result = answer_memory(command)
    if result:
        print(f"{AI_NAME}: {result}")
        continue

    if show_memory(command):
        continue

    # Save user message
    add_message("user", command)

    # AI response
    response = ask_ai(command)

    # Save AI response
    add_message("assistant", response)

    print(f"{AI_NAME}: {response}")