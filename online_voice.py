import asyncio
import edge_tts
import tempfile
import os
from pygame import mixer

VOICE = "en-US-AriaNeural"   # Female Microsoft Voice

mixer.init()

async def _speak(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        filename = f.name

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)

    mixer.music.load(filename)
    mixer.music.play()

    while mixer.music.get_busy():
        await asyncio.sleep(0.1)

    mixer.music.unload()
    os.remove(filename)


def speak_online(text):
    asyncio.run(_speak(text))