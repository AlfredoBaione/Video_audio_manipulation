import os
import random
import shutil

# Path of the initial directory
initial_directory = '...'

# Path of the final directory
final_directory = '...'

# Number of file to be randomly selected
number_of_files_to_be_selected = ...

# Obtain the list of all files in the initial directory
list_of_files = os.listdir(initial_directory)

# Randomly select the desired number of files
selected_files = random.sample(list_of_files, number_of_files_to_be_selected)

# Create the  final directory if it does not already exists
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

# Copy the selected files in the final directory
for file in selected_files:
    initial_files_path = os.path.join(initial_directory, file)
    destination_files_path = os.path.join(final_directory, file)
    shutil.copyfile(initial_files_path, destination_files_path)

print(f'{number_of_files_to_be_selected} files have been selected randomly and saved in  {final_directory}.')