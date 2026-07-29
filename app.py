from brain.ai import ask_ai

print("Juno AI Test")
print("----------------")

while True:
    user = input("Harry: ")

    if user.lower() == "exit":
        break

    print("Juno:", ask_ai(user))