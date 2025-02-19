import os
import random
from moviepy.editor import ImageClip, AudioFileClip

# Images path
images_directory = '...'
# Music path
music_directory = '...'
# Final videos path
output_directory = '...'


# Extrac the images list
images = [f for f in os.listdir(images_directory) if f.endswith(('.jpg', '.png'))]
# Extract the audio list
musics = [f for f in os.listdir(music_directory) if f.endswith(('.mp3', '.wav'))]

# Be sure there are images and music
if not images or not musics:
    print("Be sure to have at least one image and one music sample in the respective directory.")
    exit()

# Shuffle of musics and images lists
random.shuffle(images)
random.shuffle(musics)

# Minimal number of elements between images and musics
num_of_elements = min(len(images), len(musics))
# set the duration of the image
d=...
# Creating a video for each couple music-image
for i in range(num_of_elements):
    # Load image and music coupled
    img_clip = ImageClip(os.path.join(images_directory, images[i]), duration=d).resize((640, 480))
    audio_clip =AudioFileClip(os.path.join(music_directory, musics[i]))

    # Add audio to image
    video_clip = img_clip.set_audio(audio_clip)
    
    # Create the video output name
    output_path = os.path.join(output_directory,f"{os.path.splitext(images[i])[0]}_{os.path.splitext(musics[i])[0]}.mp4")
    # Write the video file
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=24)

    print(f"Video {i + 1} succesfully generated")

    # Close the clips (optional)
    img_clip.close()
    audio_clip.close()
    video_clip.close()