from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import random

def process_videos(input_folder, output_folder, duration=30):
    os.makedirs(output_folder, exist_ok=True)

    for video_file in os.listdir(input_folder):
        if video_file.endswith(".mp4"):
            video_path = os.path.join(input_folder, video_file)

            # Upload the video
            video_clip = VideoFileClip(video_path)

            # Compute the number of segments
            num_segments = int(video_clip.duration // duration)

            for i in range(num_segments):
                start_time = i * duration
                end_time = (i + 1) * duration

                # Extract the subclip
                subclip = video_clip.subclip(start_time, end_time)

                # Save the subclip in the same output direcotry
                subclip_output_path = os.path.join(output_folder, f"{video_file[:-4]}_segment_{i}.mp4")
                subclip.write_videofile(subclip_output_path, codec="libx264", audio_codec="aac")

                # Extract the audio from the subclip
                audio_output_path = os.path.join(output_folder, f"{video_file[:-4]}_audio_segment_{i}.mp3")
                subclip.audio.write_audiofile(audio_output_path)

                # Extract a frame randomly and save it
                random_frame_time = random.uniform(start_time, end_time)
                random_frame_output_path = os.path.join(output_folder, f"{video_file[:-4]}_frame_{i}.jpeg")
                video_clip.save_frame(random_frame_output_path, t=random_frame_time)

            # Close the videoclip
            video_clip.close()

if __name__ == "__main__":
    input_folder = "...."
    output_folder = "....."
    process_videos(input_folder, output_folder)