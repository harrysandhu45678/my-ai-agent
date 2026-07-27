# ===========================
# Juno Main Program
# ===========================

from config import AI_NAME, OWNER_NAME
from ai import ask_ai
from memory import remember, answer_memory, show_memory
from conversation import auto_remember, clear_history
from voice import speak, listen

print(f"{AI_NAME}: Hello {OWNER_NAME}! 👋")
print("Type 'text' for keyboard mode.")
print("Type 'voice' for microphone mode.")
print("Type 'exit' to quit.\n")

mode = "text"

while True:

    if mode == "text":
        command = input(f"{OWNER_NAME}: ")

        if command.lower() == "voice":
            mode = "voice"
            print(f"{AI_NAME}: Voice mode activated. Say 'exit' to stop voice mode.")
            continue

    else:
        command = listen()

        if command is None:
            continue

    # Exit
    if command.lower() == "exit":
        if mode == "voice":
            mode = "text"
            print(f"{AI_NAME}: Switched back to text mode.")
            continue

        speak(f"Goodbye {OWNER_NAME}!")
        break

    # Clear chat
    if command.lower() == "clear chat":
        clear_history()
        speak("Conversation cleared.")
        continue

    # Manual memory
    result = remember(command)
    if result:
        speak(result)
        continue

    # Automatic memory
    result = auto_remember(command)
    if result:
        print(f"{AI_NAME}: {result}")

    # Memory questions
    result = answer_memory(command)
    if result:
        speak(result)
        continue

    # Show memory
    result = show_memory(command)
    if result:
        speak(result)
        continue

    # AI response
    reply = ask_ai(command)
    speak(reply)