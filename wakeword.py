from openwakeword.model import Model

# Load the default wake-word models
model = Model()

def detect_wakeword(audio_chunk):
    """
    Returns the detected wake word name if one is found.
    Otherwise returns None.
    """
    predictions = model.predict(audio_chunk)

    for name, score in predictions.items():
        if score > 0.5:
            return name

    return None