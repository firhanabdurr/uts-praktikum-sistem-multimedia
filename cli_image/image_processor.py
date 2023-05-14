import argparse
import os
from PIL import Image

# Create an ArgumentParser object to handle CLI arguments
parser = argparse.ArgumentParser(description='Process and compress images')

# Add arguments for input file, output file, and compression level
parser.add_argument('input_file', help='input image file')
parser.add_argument('output_file', help='output image file')
parser.add_argument('-c', '--compress', type=int, default=70, help='compression level (0-100, default=70)')

# Parse the CLI arguments
args = parser.parse_args()

# Check if the input file exists
if not os.path.exists(args.input_file):
    print('Error: input file does not exist')
    exit()

# Open the input file using Pillow
with Image.open(args.input_file) as img:
    # Resize the image to 50% of its original size
    width, height = img.size
    img = img.resize((int(width/2), int(height/2)))

    # Convert the image to JPEG format with the specified compression level
    img.save(args.output_file, format='JPEG', quality=args.compress)

    # Print a message indicating the compression level and output file size
    output_size = os.path.getsize(args.output_file)
    print('Image compressed to {}% quality with a file size of {} bytes'.format(args.compress, output_size))
