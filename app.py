import ollama
import json

AI_NAME = "Juno"
OWNER_NAME = "Harry"

MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except:
        return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

memory = load_memory()

print(f"Welcome to {AI_NAME}!")
print(f"{AI_NAME}: Hello {OWNER_NAME}! I am ready to help you.")
print("Type 'exit' to close Juno.")

while True:
    command = input(f"{OWNER_NAME}: ")

    if command.lower().startswith("remember "): 
        fact = command[9:] 
        memory["note"] = fact
        save_memory(memory)
        print(f"{AI_NAME}: I will remember that.")
        continue

    if command.lower() == "what do you remember":
        if "note" in memory:
            print(f"{AI_NAME}: You told me: {memory['note']}")
        else:
            print(f"{AI_NAME}: I don't remember anything yet.")
        continue

    if command.lower() == "what is my favourite colour":
        if "note" in memory:
            print(f"{AI_NAME}: Your favourite colour is black.")
        else:
            print(f"{AI_NAME}: I don't know your favourite colour yet.")
        continue

    if command.lower() == "exit":
        print(f"{AI_NAME}: Goodbye {OWNER_NAME}! See you soon.")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": f"""
You are {AI_NAME}, a friendly female AI assistant.

Your owner's name is {OWNER_NAME}.

Always call him Harry.

Be polite, intelligent, helpful and friendly.

Keep your answers short unless Harry asks for details.
"""
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    print(f"{AI_NAME}: {response['message']['content']}")