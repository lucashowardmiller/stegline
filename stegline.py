# used to handle the command line args
import argparse
# import os for file check
import os
import sys
# packaged implementations of steg functions
from stegline_modules import fileModule, lsbModule, manipulationModule, metaModule

# TODO add support for no outdir and then use tempfiles, + opt args in def()
# TODO standardize report location and limit code re-use


# will increment to 1.0 when everything in spec works, and then update status to something less broken sounding
__authors__ = ["Lucas Miller"]
__description__ = "Handles varies image manipulation modules as specified"
__maintainer__ = "Lucas Miller"
__version__ = "0.0"
__status__ = "Prototype"
__license__ = "MIT"

# creates a parser to handle in/out filepaths
moduleParser = argparse.ArgumentParser(description='Select what modules to use')
moduleParser.add_argument("INPUT_FILE", help="Path to input file")
moduleParser.add_argument("OUTPUT_FOLDER", help="Path to output file")

# creates a parser to handle modules
moduleParser.add_argument('-b', action="store_true", default=False, help='Enables LSB module')
moduleParser.add_argument('-m', action="store_true", default=False, help='Enables metadata module')
moduleParser.add_argument('-x', action="store_true", default=False, help='Enables exif module')
moduleParser.add_argument('-t', action="store_true", default=False, help='Enables text find modules')
moduleParser.add_argument('-f', action="store_true", default=False, help='Enables file info modules')
moduleParser.add_argument('-s', action="store_true", default=False, help='Enables strings module')
moduleParser.add_argument('-z', action="store_true", default=False, help='Enables resize module')
moduleParser.add_argument('-a', action="store_true", default=False, help='Enables all modules')


# Parsing and using the arguments
args = moduleParser.parse_args()

input_file = args.INPUT_FILE
output_folder = args.OUTPUT_FOLDER

if not os.path.isfile(input_file):
    print("INPUT_FILE must be a file")
    sys.exit(1)

if not os.path.isdir(output_folder):
    print("output_folder must be a directory")
    sys.exit(1)

# radical and needed lines
reportLocation = output_folder + '/' + 'report.txt'
f = open(reportLocation, "a+")
f.write(" __  _____  __  ___   __   _____    __  __  " + "\n")
f.write("/ _\/__   \/__\/ _ \ / /   \_   \/\ \ \/__\ " + "\n")
f.write("\ \   / /\/_\ / /_\// /     / /\/  \/ /_\\  " + "\n")
f.write("_\ \ / / //__/ /_\\\/ /___/\/ /_/ /\  //__  " + "\n")
f.write("\__/ \/  \__/\____/\____/\____/\_\ \/\__/   " + "\n")
f.write("Created by: Lucas Miller" + "\n")
f.write("github.com/lucashowardmiller/stegline" + "\n\n")
f.close()

# runs the functions for specified args
argsModules = moduleParser.parse_args()
if argsModules.b or argsModules.a:
    lsbModule.lsb(input_file, output_folder)

if argsModules.m or argsModules.a:
    metaModule.metadata(input_file, output_folder)

if argsModules.x or argsModules.a:
    metaModule.exif(input_file, output_folder)

if argsModules.t or argsModules.a:
    manipulationModule.text_find(input_file, output_folder)

if argsModules.f or argsModules.a:
    fileModule.filecheck(input_file, output_folder)

if argsModules.s or argsModules.a:
    metaModule.strings(input_file, output_folder)

# TODO enable resize again for -a once it stops breaking files
if argsModules.z:
    manipulationModule.resize(input_file, output_folder)

# fixes header on multiple runs
f = open(reportLocation, "a+")
f.write("\n")
f.close()


