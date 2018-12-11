import cv2
import numpy as np
from PIL import Image

# used to get file extension
import os
# used to modify bytes
import mmap
# used to copy the mmap image file
import shutil
import pytesseract
import datetime


# https://motherboard.vice.com/en_us/article/qkjbkw/hack-this-edit-an-image-with-python

# TODO add bluring and such for better tesserect handeling / change to opencv
# TODO add baseline functionality and create some sort of report

def resize(input_file, output_folder):
    file_extension = os.path.splitext(input_file)[1][1:]
    reportLocation = output_folder + '/' + 'report.txt'
    extractionFolder = output_folder + '/' + 'SteglineGenerated'
    copiedimage = extractionFolder + '/' + "copyOfImage" + str(os.getpid()) + "." + file_extension

    if not os.path.exists(extractionFolder):
        os.mkdir(extractionFolder)

    shutil.copy2(input_file, copiedimage)

    f = open(reportLocation, "a+")


    # gets the extension as resize works differently on each image type
    # jpg trigger this could probably use magic bytes
    if file_extension == 'jpg':
        f.write("Resize Module was ran on the image." + "\n")

        # the bytes prefixing jpgs img size controls
        size_controls_prefix = bytearray([0xFF, 0xC0, 0x00, 0x11, 0x08])
        new_size = bytearray([0x01, 0xE1, 0x01, 0xD9])

        with open(copiedimage, 'r+b') as img:
            imgByteMap = mmap.mmap(img.fileno(), 0)
            print(imgByteMap.readline())

    else:
        # prints if file_extension has no matches
        f.write("Resize Module was not ran on the image, as no matching compatible file types were found." + "\n")
    f.close()

    print("resize end")


def shiftcolormap(input_file):

    print("end of colormap")


def textfind(input_file, output_folder):

    file_extension = os.path.splitext(input_file)[1][1:]
    reportLocation = output_folder + '/' + 'report.txt'
    extractionFolder = output_folder + '/' + 'SteglineGenerated'
    copiedimage = extractionFolder + '/' + "ocrpreprocess" + "." + file_extension

    if not os.path.exists(extractionFolder):
        os.mkdir(extractionFolder)

    shutil.copy2(input_file, copiedimage)

    f = open(reportLocation, "a+")
    f.write("\n" + "Text found in the image:" + "\n")
    f.write(textsearch(copiedimage))
    f.write("\n\n")
    f.close()

    print('end of textfind()')


# changes tints to look for hidden text
def imagemanipulation(input_file, output_folder):
    print('end of image manipulation')


# will clean an image before pytesseract
def textsearch(input_file: Image):
    return pytesseract.image_to_string(Image.open(input_file))

