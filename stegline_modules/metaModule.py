#used for mkdir
import os
#used to get exif data in exif()
import exifread
#used to call strings in strings()
import subprocess
#used for iterating through strings-ouput.txt to look for .{.} and NCL/SKY
import re

def metadata(input_file, output_folder):
    # this is on the backburner for a bit
    # not very ctf nor super flashy
    # also pretty jank
    stat_info = os.stat(input_file)
    print("Metadata is not implemented")


def exif(input_file, output_folder):
    img = open(input_file, 'rb')
    tags = exifread.process_file(img)
    reportLocation = output_folder + '/' + 'report.txt'
    f = open(reportLocation, "a+")
    f.write("Exif Data: \n")

    for tag in tags.keys():
        f.write("Key: %s, value %s" % (tag, tags[tag]) + "\n")
    f.write("\n")

    f.close()


def strings(input_file, output_folder):
    # used to match ABCD{FLAG_w@CkY} (not currently used)
    flag_brackets = re.compile('.*{.*}')
    # used to match NCL/SKY, can false match with something like NKL-ABCD-1234
    flag_skyncl = re.compile('[NCLSKY]{3}-[a-zA-Z]{3}-[0-9]{4}')


    reportLocation = output_folder + '/' + 'report.txt'
    extractionFolder = output_folder + '/' + 'SteglineGenerated'
    stringLocation = extractionFolder + '/' + 'strings-output.txt'


    if not os.path.exists(extractionFolder):
        os.mkdir(extractionFolder)

    stingLocation = open(stringLocation, "w")

    subprocess.call(["strings", input_file], stdout=stingLocation)
    with open(stringLocation, 'r') as sL:
        skynclMatch = re.findall(flag_skyncl, sL.read())
        bracketMatch = re.findall(flag_brackets, sL.read())
    sL.close()

    f = open(reportLocation, "a+")
    if len(bracketMatch) > 0 or len(skynclMatch) > 0:
        f.write("\n" + "Potential flags found using Strings:" + "\n")

        for match in bracketMatch:
            f.write("Possible Flag: " + match)

        for match in skynclMatch:
            f.write("Possible Flag: " + match)
    else:
        f.write("\n" + "No flags in SKY/NCL format or .*{.*} format were found")
    f.close()
    print("end of strings")