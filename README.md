# stegline
Stegline is a repackaging of existing programs, non-novel implemenations of python functions, and maybe something new.

StegLine will put the results of each modules analysis into the output_folder.

### Usage:

	"python stegline.py StegImage.jpg outdir -f"

                    
### Dependencies:

(It's recomended you create a virtual enviroment for running the project)

Current Dependencies:
- pip install Pillow
- Binwalk (from source)
- brew install tesseract --HEAD
- pip install pytesseract
- pip install exifread
