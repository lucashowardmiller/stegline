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


# changes colormaps to look for hidden text
def shift_colormap(input_file):

    print("end of colormap")


# changes tints to look for hidden text
def image_manipulation(input_file, output_folder):
    print('end of image manipulation')


# wraps image_ocr() to print out ocr results nicely to the report
def text_find(input_file, output_folder):

    file_extension = os.path.splitext(input_file)[1][1:]
    reportLocation = output_folder + '/' + 'report.txt'
    extractionFolder = output_folder + '/' + 'SteglineGenerated'
    copiedimage = extractionFolder + '/' + "ocrpreprocess" + "." + file_extension

    if not os.path.exists(extractionFolder):
        os.mkdir(extractionFolder)

    shutil.copy2(input_file, copiedimage)

    f = open(reportLocation, "a+")
    f.write("\n" + "Text found in the image:" + "\n")
    f.write(image_ocr(copiedimage, output_folder))
    f.write("\n\n")
    f.close()

    print('end of text_find()')


# will clean an image before pytesseract
def image_ocr(input_file, output_folder):
    stringsList = []
    extractionFolder = output_folder + '/' + 'SteglineGenerated'
    file_extension = os.path.splitext(input_file)[1][1:]
    copiedimage = extractionFolder + '/' + "processedWithOCR" + "." + file_extension
    copiedimage2 = extractionFolder + '/' + "processedWithOCR2" + "." + file_extension

    if not os.path.exists(extractionFolder):
        os.mkdir(extractionFolder)

    image = cv2.imread(input_file)

    # unedited image
    stringsList.append(pytesseract.image_to_string(image))

    # pure white text filter
    th, inverseBinaryFiltered = cv2.threshold(cv2.bitwise_not(image), 5, 255, cv2.THRESH_BINARY)
    stringsList.append(pytesseract.image_to_string(inverseBinaryFiltered))

    # normal text


    # noisy background


    # noisy + colorful

    return text_process(stringsList)


# attempts to return the string in the list that looks the most like text
def text_process(text):

    # used to track the most text looking text
    selected_index = 0

    # current version determines result on non whitespace chars produced, this generally tracks with the best ocr
    # this will be swapped out eventually to filter for words/flags
    for index, result in enumerate(text):
        if len(result) - text.count(' ') > len(text[selected_index]) - text[selected_index].count(' '):
            selected_index = index
    return text[index]

    print("end of text process")

