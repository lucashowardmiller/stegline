#used to handle the command line args
import argparse
#import os for file check
import os
import sys
#lsb
import lsbModule
#meta
import metaModule
#text find
import manipulationModuale
#ext and type
import fileModule
#TODO Resize

__authors__ = "Lucas Miller"
__description__ = "Handles varies image manipulation modules as specified"
__maintainer__ = "Lucas Miller"
__version__ = "0.0"
__status__ = "Prototype"
__license__ = "CC BY-NC-ND"

#creates a parser to handle in/out filepaths
fileParser = argparse.ArgumentParser(description='Select in/out filepaths')
fileParser.add_argument("INPUT_FILE", help="Path to input file")
#fileParser.add_argument("OUTPUT_FILE", help="Path to output file")

#creates a parser to handle modules
moduleParser = argparse.ArgumentParser(description='Select what modules to use')
moduleParser.add_argument('-b', action="store_true", default=False, help='Enables LSB module')
moduleParser.add_argument('-m', action="store_true", default=False, help='Enables metadata module')
moduleParser.add_argument('-x', action="store_true", default=False, help='Enables exif module')
moduleParser.add_argument('-t', action="store_true", default=False, help='Enables text find modules')
moduleParser.add_argument('-f', action="store_true", default=False, help='Enables file mis-match modules')


# Parsing and using the arguments
args = fileParser.parse_args()

input_file = args.INPUT_FILE
print(input_file)
#output_file = args.OUTPUT_FILE
#print(output_file)

if os.path.isfile(input_file):
    print("is file")
else:
    print("INPUT_FILE must be a file")
    sys.exit(1)


#printout what mods args are enabled and runs the functions
argsModules = moduleParser.parse_args()
if argsModules.b:
    print("LSB turned on")
    lsbModule.lsb(input_file)
else:
    print("LSB turned off")

if argsModules.m:
    print("Metadata turned on")
    metaModule.metadata(input_file)
else:
    print("Metadata turned off")

if argsModules.x:
    print("exif turned on")
    metaModule.exif(input_file)
else:
    print("exif turned off")

if argsModules.t:
    print("Text find turned on")
    manipulationModuale.textfind(input_file)
else:
    print("Text find turned off")

if argsModules.f:
    print("File check turned on")
    fileModule.filecheck(input_file)
else:
    print("File check turned off")

