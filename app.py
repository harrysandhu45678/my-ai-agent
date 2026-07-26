import ollama

AI_NAME = "Juno"
OWNER_NAME = "Harry"

print(f"Welcome to {AI_NAME}!")
print(f"{AI_NAME}: Hello {OWNER_NAME}! I am ready to help you.")
print("Type 'exit' to close Juno.")

while True:
    command = input(f"{OWNER_NAME}: ")

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