import argparse
import os
from PIL import Image

# Create an ArgumentParser object to handle CLI arguments
parser = argparse.ArgumentParser(description='Process and compress images')

# Add arguments for input file, output file, and compression level
parser.add_argument('input_file', help='input image file')
parser.add_argument('output_file', help='output image file')
parser.add_argument('-c', '--compress', type=int, default=70, help='compression level (0-100, default=70)')


args = parser.parse_args()


if not os.path.exists(args.input_file):
    print('Error: input file does not exist')
    exit()


with Image.open(args.input_file) as img:
    
    width, height = img.size
    img = img.resize((int(width/2), int(height/2)))

    
    img.save(args.output_file, format='JPEG', quality=args.compress)

    
    output_size = os.path.getsize(args.output_file)
    print('Image compressed to {}% quality with a file size of {} bytes'.format(args.compress, output_size))
