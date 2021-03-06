# used for mkdir
import os
# used to get exif data in exif()
import exifread
# used to call strings in strings()
import subprocess
# used for iterating through strings-ouput.txt to look for .{.} and NCL/SKY
import re
from stegline_modules import string_id


def metadata(input_file, output_folder):
    # this is on the backburner for a bit
    # not very ctf nor super flashy
    # also pretty jank
    stat_info = os.stat(input_file)


def exif(input_file, output_folder):
    img = open(input_file, 'rb')
    tags = exifread.process_file(img)
    reportLocation = output_folder + '/' + 'report.txt'
    f = open(reportLocation, "a+")
    f.write("Exif Data: \n")

    for tag in tags.keys():
        # limits really verbose tags
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            f.write("%s, value %s" % (tag, tags[tag]) + "\n")
    f.write("\n")

    f.close()


def strings(input_file, output_folder):
    # TODO refactor with new id all ctf strings method once completed
    # used to match ABCD{FLAG_w@CkY}
    flag_brackets = re.compile('.*{.*}')
    # used to match NCL/SKY, can false match with something like NKL-ABCD-1234
    # improved (?i)(NCL|SKY)-[a-zA-Z]{4}-[0-9]{4}, figure out how to return whole string only NCL/SKY now
    flag_skyncl = re.compile('[NCLSKYnclsky]{3}-[a-zA-Z]{4}-[0-9]{4}')
    # hactober/generic, can false match with something like glaf-dkskdjsk
    flag_generic = re.compile('[FLAGflag]{4}-.*')

    reportLocation = output_folder + '/' + 'report.txt'
    extractionFolder = output_folder + '/' + 'SteglineGenerated'
    stringLocation = extractionFolder + '/' + 'strings-output.txt'

    if not os.path.exists(extractionFolder):
        os.mkdir(extractionFolder)

    stingLocation = open(stringLocation, "w")

    subprocess.call(["strings", input_file], stdout=stingLocation)
    with open(stringLocation, 'r') as sL:
        string_file_lines = sL.readlines()
    sL.close()

    matched_strings = string_id.return_ctf_flags(string_file_lines)

    f = open(reportLocation, "a+")
    if len(matched_strings) > 0:
        f.write("\n" + "Potential flags found using Strings:" + "\n")

        for match in matched_strings:
            f.write("Possible CTF Flag: " + match)

    else:
        f.write("\n" + "Strings results: ")
        f.write("\n" + "No flags in SKY/NCL format or .*{.*} format were found")
    f.close()
