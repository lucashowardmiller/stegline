import os
import subprocess


# import binwalk
# todo find python bindings


def filecheck(input_file, output_folder):
    file_extension = os.path.splitext(input_file)
    reportLocation = output_folder + '/' + 'report.txt'
    extractionFolder = output_folder + '/' + 'report.txt'
    f = open(reportLocation, "w+")
    f.write("File data: \n")


    print("end of filecheck")
