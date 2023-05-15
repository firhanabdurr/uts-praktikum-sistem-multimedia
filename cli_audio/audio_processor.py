import argparse
import os
from pydub import AudioSegment

# Create an ArgumentParser object to handle CLI arguments
parser = argparse.ArgumentParser(description='Process and compress audio files')

# Add arguments for input file, output file, and compression level
parser.add_argument('input_file', help='input audio file')
parser.add_argument('output_file', help='output audio file')
parser.add_argument('-b', '--bitrate', type=str, default='128k', help='bitrate for output file (default=128k)')

# Parse the CLI arguments
args = parser.parse_args()

# Check if the input file exists
if not os.path.exists(args.input_file):
    print('Error: input file does not exist')
    exit()

# Open the input file using PyDub
audio = AudioSegment.from_file(args.input_file)

# Apply a fade-in effect to the first 3 seconds of the audio
fade_in = audio[:3000].fade_in(1000)

# Apply a fade-out effect to the last 3 seconds of the audio
fade_out = audio[-3000:].fade_out(1000)

# Combine the faded audio with the original audio without the first and last 3 seconds
processed_audio = fade_in + audio[3000:-3000] + fade_out

# Export the processed audio to the specified output file with the specified bitrate
processed_audio.export(args.output_file, format='mp3', bitrate=args.bitrate)

# Print a message indicating the bitrate and output file size
output_size = os.path.getsize(args.output_file)
print('Audio compressed to {} bitrate with a file size of {} bytes'.format(args.bitrate, output_size))