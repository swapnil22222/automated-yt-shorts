import random
from groq import Groq

client = Groq(api_key="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")

# load startup list
with open("startups.txt","r",encoding="utf-8") as f:
    startups = [s.strip() for s in f.readlines()]

# remove invalid names
startups = [s for s in startups if len(s) > 2 and "http" not in s]

# pick random startup
startup = random.choice(startups)

prompt = f"""
Create a YouTube Shorts script about the startup {startup}.

Language: Hinglish (Hindi + English mix).

Length: 140-160 words.

Structure:
1 Hook
2 Quick facts about the startup
1 Ending line about impact, valuation, or success.

Style:
Short sentences.
Engaging.
Good for narration.

Example tone:
"Instagram shuru hua ek simple photo sharing app ke roop mein...
sirf 2 mahine mein 1 million users...
aaj billions log use karte hain."
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "You are a script writer for viral YouTube Shorts."
        },
        {
            "role": "user",
            "content": f"""
Write a 240-260 word Hinglish narration about the startup {startup}.

Rules:
- DO NOT say things like 'Here is a script'.
- DO NOT mention YouTube, script, narrator, or instructions.
- Only output the narration text.

Style:
Short sentences.
Dramatic storytelling.
Good for voice narration.

Example style:
"Instagram shuru hua ek simple photo sharing app ke roop mein...
sirf 2 mahine mein 1 million users...
aaj billions log use karte hain."
"""
        }
    ]
)

script = response.choices[0].message.content

print("\nStartup Selected:", startup)
print("\nGenerated Script:\n")
print(script)

with open("script.txt","w",encoding="utf-8") as f:
    f.write(script)