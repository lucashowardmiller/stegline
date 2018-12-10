import cv2
import numpy as np
from PIL import Image

# used to get file extension
import os
# used to modify bytes
import mmap
# used to copy the mmap image file
import shutil


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
    print(copiedimage)
    img_copy_location = ""
    # gets the extension as resize works differently on each image type
    # jpg trigger this could probably use magic bytes
    if file_extension == 'jpg':
        # the bytes prefixing jpgs img size controls
        size_controls_prefix = bytearray([0xFF, 0xC0, 0x00, 0x11, 0x08])
        new_size = bytearray([0x01, 0xE1, 0x01, 0xD9])
        with open(copiedimage, 'r+b') as img:
            data = bytearray(img.read())
            print("match jpg")
            imgByteMap = mmap.mmap(img.fileno(), 0)
            print(imgByteMap.readline())

            # might change the control bytes
            imgByteMap[imgByteMap.find(size_controls_prefix) + 5: imgByteMap.find(size_controls_prefix) + 9] = new_size
            # imgByteMap.write(imgByteMap.readline(), new_size)
            print(imgByteMap.find(size_controls_prefix))

    print("resize end")

def shiftcolormap(input_file):

    print("end of colormap")

def textfind(input_file, output_folder):
    print('end of textfind()')


# changes tints to look for hidden text
def imagemanipulation(input_file, output_folder):
    print('end of image manipulation')


def invert(input_file, output_folder):
    print("placeholder for invert ")


def textsearch(input_file):
    return ("neat-o stringo")
