# TODO writ#TODO write metadata handler
# TODO "write" exif handler

import os
from PIL import Image
import exifread


def metadata(input_file, output_folder):
    # this is on the backburner for a bit
    # not very ctf nor super flashy
    # also pretty jank
    stat_info = os.stat(input_file)
    print("Meta is not implemnted")


def exif(input_file, output_folder):
    img = open(input_file, 'rb')
    tags = exifread.process_file(img)

    f = open("report.txt", "w+")
    f.write("Exif Data: \n")

    for tag in tags.keys():
        f.write("Key: %s, value %s" % (tag, tags[tag]) + "\n")
