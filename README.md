# stegline
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


### Dependencies:

Dependencies are a little unstable.

Current Dependencies:
- Pillow 5.3.0
- Binwalk (from source, pypi package does not work)
- ExifRead 2.1.2
- Pytesseract
- cv2
