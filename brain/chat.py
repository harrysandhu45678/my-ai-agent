from system.assistant import Assistant
from brain.ai import ask_ai
from brain.commands import process_command

assistant = Assistant()


def start_chat():

    print("=================================")
    print("        Juno Version 11")
    print("=================================\n")

    while True:

        command = input("Harry: ").strip()

        # Exit
        if command.lower() == "exit":
            print("Juno: Goodbye Harry!")
            break

        # Sleep
        if command.lower() == "sleep":
            print("Juno:", assistant.sleep())
            continue

        # Wake
        if command.lower() == "wake up":
            print("Juno:", assistant.wake())
            continue

        # Status
        if command.lower() == "status":
            print("Juno:", assistant.status())
            continue

        # Ignore commands while sleeping
        if not assistant.is_awake():
            print("Juno: I'm sleeping. Say 'wake up' to wake me.")
            continue

        # Built-in commands
        result = process_command(command)

        if result:
            print("Juno:", result)
            continue

        # AI Chat
        reply = ask_ai(command)
        print("Juno:", reply)