from openwakeword.model import Model

print("Loading wake-word models...")

model = Model()

print("Available wake words:")

for wakeword in model.models.keys():
    print("-", wakeword)

print("\nOpenWakeWord loaded successfully!")