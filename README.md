# stegline

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/lucashowardmiller/stegline/blob/master/license.md)   [![Python](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)


Stegline is a repackaging of existing programs, non-novel implemenations of python functions, and maybe something new.

Stegline is designed to unify existing tools fractured capibility.

StegLine will put the results of each modules analysis into the output_folder.

### Usage:

	"python stegline.py StegImage.jpg outdir (args)"

### Current Functionality:
- Getting some ctf's flags automatically from the strings and output them to a report
- Outputting an image's exif tags and output them to a report
- Seeing if a files magic bytes matches its file extension
- Can detect hidden files in an image
- OCR capabilities
- Detecting data hidden with size control manipulation
- Detecting data hidden with color channel manipulation


### Dependencies:

Dependencies are a little unstable.

Current Dependencies:
- Pillow 5.3.0
- Binwalk
- cv2
