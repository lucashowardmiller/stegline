import os
import subprocess


# import binwalk
# todo find python bindings


def filecheck(input_file, output_folder):
    file_extension = os.path.splitext(input_file)

    print("end of filecheck")
