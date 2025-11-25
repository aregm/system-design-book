#!/usr/bin/env python3

"""
Convert VTT subtitles to plain text

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
"""

import webvtt
import argparse

parser = argparse.ArgumentParser(
                    prog='vttconverter',
                    description='Convert VTT subtitles to plain text',
                    epilog='Text at the bottom of help')
parser.add_argument('input', type=str, help='Input VTT file')
parser.add_argument('--output', '-o', type=str, help='Output text file')
parser.add_argument('--oneline', '-1', action='store_true', default=True, help='Output all text in one line')
args = parser.parse_args()

try:
    vtt = webvtt.read(args.input)
except FileNotFoundError:
    print(f"ERROR: File {args.input} not found.")
    exit(1)
transcript = ""

lines = []
for line in vtt:
    # Strip the newlines from the end of the text.
    # Split the string if it has a newline in the middle
    # Add the lines to an array
    lines.extend(line.text.strip().splitlines())

# Remove repeated lines
separator = " " if args.oneline else "\n"
previous = None
for line in lines:
    if line == previous:
       continue
    transcript += separator + line
    previous = line

if args.output:
    with open(args.output, 'w') as f:
        f.write(transcript)
else:
    print(transcript)
