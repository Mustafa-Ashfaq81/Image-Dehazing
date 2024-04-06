from PIL import Image
import os

def convert_to_png(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all files in the input directory
    files = os.listdir(input_dir)

    # Iterate over each file
    for file in files:
        if file.endswith('.jpg') or file.endswith('.jpeg'):
            # Open the image
            image_path = os.path.join(input_dir, file)
            img = Image.open(image_path)

            # Construct the output file path with .png extension
            output_path = os.path.join(output_dir, os.path.splitext(file)[0] + '.png')

            # Convert and save as PNG
            img.save(output_path, format='PNG')
            print(f"Converted {file} to PNG")

# Specify input and output directories
input_directory = 'data/RESIDE-OUT/test/hazy'  # Change this to your input directory
output_directory = 'testhazyPng'  # Change this to your output directory

# Convert JPEG images to PNG
convert_to_png(input_directory, output_directory)
