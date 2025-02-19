from pydub import AudioSegment

import os

def split_mp3_files(input_folder, output_folder, segment_length=30):
    # Create the output directory
    os.makedirs(output_folder, exist_ok=True)

    # Elaborate each file in the input directory
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            input_path = os.path.join(input_folder, filename)
            
            # Upload the mp3 file
            audio = AudioSegment.from_mp3(input_path)

            # Compute the duration of the mp3 file
            total_duration = len(audio)

            # Compute the desired duration of the mp3 file 
            segment_length_ms = segment_length * 1000

            # Compute the number of segments
            num_segments = total_duration // segment_length_ms

            # Divide the mp3 file into 30 seconds segments
            for i in range(num_segments):
                start_time = i * segment_length_ms
                end_time = (i + 1) * segment_length_ms
                segment = audio[start_time:end_time]

                # Create the file output name
                output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_segment_{i + 1}.mp3")

                # Save the segment as mp3
                segment.export(output_file, format="mp3")

            print(f"The file {filename} has been divided into 30 seconds segments.")

# Example
input_folder_path = "..."
output_folder_path = "...."
split_mp3_files(input_folder_path, output_folder_path)