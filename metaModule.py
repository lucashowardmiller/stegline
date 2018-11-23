#TODO writ#TODO write metadata handler
#TODO "write" exif handler

import os
from PIL import Image
import exifread


def metadata (input_file, output_folder):
   stat_info = os.stat(input_file)

   print()
def exif(input_file, output_folder):
  # exifImage = Image.open("input_file")
  f = open(input_file, 'rb')
  tags = exifread.process_file(f)
  print(tags)