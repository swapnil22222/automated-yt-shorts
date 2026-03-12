import math

def format_time(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

# read script
with open("script.txt","r",encoding="utf-8") as f:
    text = f.read()

sentences = [s.strip() for s in text.split("\n") if s.strip()]

words_per_second = 2.5
current_time = 0

with open("subtitles.srt","w",encoding="utf-8") as f:
    for i, sentence in enumerate(sentences, start=1):

        word_count = len(sentence.split())
        duration = word_count / words_per_second

        start = format_time(current_time)
        end = format_time(current_time + duration)

        f.write(f"{i}\n")
        f.write(f"{start} --> {end}\n")
        f.write(sentence + "\n\n")

        current_time += duration

print("Subtitles generated successfully")