# ==========================
# Juno Version 10
# ==========================

from config import AI_NAME, OWNER_NAME
from ai import ask_ai
from memory import remember, answer_memory, show_memory
from conversation import auto_remember, clear_history
from voice import speak, listen, enable_voice, disable_voice, voice_enabled
from assistant import Assistant

assistant = Assistant()
disable_voice()
assistant.greet()

print(f"{AI_NAME}: Hello {OWNER_NAME}! 👋")
print("Type 'text' for keyboard mode.")
print("Type 'voice' for microphone mode.")
print("Type 'exit' to quit.\n")

mode = "text"

while True:
    if mode == "text":
        disable_voice()
        command = input(f"{OWNER_NAME}: ").strip()
        if command.lower() == "voice":
            mode = "voice"
            enable_voice()
            print("DEBUG:",voice_enabled())
            speak("Voice mode activated.")
            continue
    else:
        enable_voice()
        command = listen()
        if command is None:
            continue

    command = command.strip()

    if not assistant.is_awake():
        if command.lower() == "wake up":
            assistant.wake()
        else:
            speak("I'm sleeping. Say wake up.") if voice_enabled() else print(f"{AI_NAME}: I'm sleeping. Type wake up.")
        continue

    if command.lower() == "sleep":
        assistant.sleep(); continue
    if command.lower() == "wake up":
        assistant.wake(); continue
    if command.lower() == "status":
        assistant.status(); continue

    if command.lower() == "exit":
        if mode == "voice":
            mode = "text"
            disable_voice()
            print(f"{AI_NAME}: Switched back to text mode.")
            continue
        print(f"{AI_NAME}: Goodbye {OWNER_NAME}!")
        break

    if command.lower() == "clear chat":
        clear_history()
        speak("Conversation cleared.") if voice_enabled() else print(f"{AI_NAME}: Conversation cleared.")
        continue

    for func in (remember, answer_memory, show_memory):
        result = func(command)
        if result:
            speak(result) if voice_enabled() else print(f"{AI_NAME}: {result}")
            break
    else:
        auto = auto_remember(command)
        if auto:
            print(f"{AI_NAME}: {auto}")
        reply = ask_ai(command)
        speak(reply) if voice_enabled() else print(f"{AI_NAME}: {reply}")
