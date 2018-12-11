# stegline
Stegline is a repackaging of existing programs, non-novel implemenations of python functions, and maybe something new.

Stegline is designed to unify existing tools fractured capibility.

StegLine will put the results of each modules analysis into the output_folder.

### Usage:

	"python stegline.py StegImage.jpg outdir (args)"

### Current Functionality:
- Can get some ctf's flags automatically from the strings and output them to a report
- Can output an images exif tages and output them to a report
- Can see if a files magic bytes match its file extension
- Can detect hidden files in an image


### Dependencies:

Dependincies are a little unstable.

Current Dependencies:
- Pillow 5.3.0
- Binwalk (from source, pypi package does not work)
- ExifRead 2.1.2
