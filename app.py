import json
import os
import ollama

AI_NAME="Juno"
OWNER_NAME="Harry"
MEMORY_FILE="memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE,"r") as f:
            return json.load(f)
    return {}

def save_memory(mem):
    with open(MEMORY_FILE,"w") as f:
        json.dump(mem,f,indent=4)

memory=load_memory()

def ask_llama(prompt):
    r=ollama.chat(
        model="llama3.2",
        messages=[
            {"role":"system","content":"You are Juno, a helpful AI assistant."},
            {"role":"user","content":prompt},
        ],
    )
    return r["message"]["content"]

def remember(command):
    if not command.lower().startswith("remember "):
        return False
    fact=command[9:]
    if " is " not in fact:
        print(f"{AI_NAME}: Say 'remember my pet is Rocky'")
        return True
    key,value=fact.split(" is ",1)
    memory[key.strip()]=value.strip()
    save_memory(memory)
    print(f"{AI_NAME}: I'll remember that.")
    return True

def show_memory(command):
    if command.lower()!="what do you remember":
        return False
    if not memory:
        print(f"{AI_NAME}: I don't remember anything yet.")
    else:
        print(f"{AI_NAME}: Here's everything I know:")
        for k,v in memory.items():
            print(f"- {k}: {v}")
    return True

def answer_memory(command):
    c=command.lower().strip().rstrip("?")
    if c=="tell me about myself":
        if memory:
            for k,v in memory.items():
                print(f"{k}: {v}")
        else:
            print(f"{AI_NAME}: I don't know much about you yet.")
        return True
    if c=="who am i":
        print(f"{AI_NAME}: You are {OWNER_NAME}.")
        return True
    mapping={
        "where do i live":"my city",
        "when is my birthday":"my birthday",
        "what is my pet":"my pet",
        "which bike do i have":"my bike",
        "what is my favourite colour":"my favourite colour",
        "what is my favorite color":"my favorite color",
    }
    if c in mapping:
        key=mapping[c]
        if key in memory:
            print(f"{AI_NAME}: {memory[key]}")
        else:
            print(f"{AI_NAME}: I don't know that yet.")
        return True
    if c.startswith("what is my "):
        key="my "+c[11:]
        if key in memory:
            print(f"{AI_NAME}: {memory[key]}")
        else:
            print(f"{AI_NAME}: I don't know your {c[11:]} yet.")
        return True
    return False

print(f"{AI_NAME}: Hello {OWNER_NAME}! I am ready to help you.")
print("Type 'exit' to close Juno.")

while True:
    command=input(f"{OWNER_NAME}: ")
    if remember(command): continue
    if show_memory(command): continue
    if answer_memory(command): continue
    if command.lower()=="exit":
        print(f"{AI_NAME}: Goodbye!")
        break
    print(f"{AI_NAME}: {ask_llama(command)}")
