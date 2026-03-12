import asyncio
import edge_tts

VOICE = "en-IN-NeerjaNeural"

async def generate_voice():
    with open("script.txt", "r", encoding="utf-8") as f:
        text = f.read()

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="+20%"   # faster narration
    )

    await communicate.save("voice.mp3")
    print("Voice generated successfully: voice.mp3")

asyncio.run(generate_voice())