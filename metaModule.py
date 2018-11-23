#TODO writ#TODO write metadata handler
#TODO "write" exif handler

import os
from PIL import Image
import exifread


def metadata (input_file, output_folder):
   stat_info = os.stat(input_file)

   print()
def exif(input_file, output_folder):
  img = open(input_file, 'rb')
  tags = exifread.process_file(img)
  #TODO format exif strings and create a report


  f = open("report.txt", "w+")

  for tag in tags.keys():
      if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):

          f.write("Key: %s, value %s" % (tag, tags[tag]) + "\n")