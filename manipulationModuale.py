from PIL import Image
import pytesseract
import cv2
import os

#TODO add bluring and such for better tesserect handeling / change to opencv

def textfind(input_file):
    baseline = textsearch(input_file)

    print()


def imagemanipulation(input_file):

    print()


def textsearch(input_file):
    image = cv2.imread(input_file)
    orig = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return text

    print(text)