import os
import shutil

# Source folder
source_folder = "source"

# Destination folder
destination_folder = "destination"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move all JPG files
for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"{file} moved successfully!")

print("All JPG files moved successfully.")