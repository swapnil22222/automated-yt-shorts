import os
import random
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

# load audio
audio = AudioFileClip("voice.mp3")

# choose random background
bg_folder = "backgrounds"
video_file = random.choice(os.listdir(bg_folder))
video_path = os.path.join(bg_folder, video_file)

video = VideoFileClip(video_path)

# loop video until audio duration
video = video.loop(duration=audio.duration)

# resize to vertical
video = video.resize(height=1920)

# attach audio
video = video.set_audio(audio)

# subtitle generator
generator = lambda txt: TextClip(
    txt,
    font="Arial-Bold",
    fontsize=70,
    color="white",
    stroke_color="black",
    stroke_width=2
)

subtitles = SubtitlesClip("subtitles.srt", generator)

# position subtitles
subtitles = subtitles.set_position(("center","bottom"))

# combine video + subtitles
final = CompositeVideoClip([video, subtitles])

# export
final.write_videofile("short.mp4", fps=30)

print("Short video created successfully")