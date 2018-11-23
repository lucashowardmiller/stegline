import os
import binwalk
import subprocess
from subprocess import call

# todo find python bindings



def filecheck(input_file, output_folder):
    file_extension = os.path.splitext(input_file)

    print(file_extension)
    for module in binwalk.scan(input_file, signature=True, quiet=True):
        print("%s Results:" % module.name)
        for result in module.results:
            print("\t%s    0x%.8X    %s" % (result.file.name, result.offset, result.description))

    reportLocation = output_folder + '/' + 'report.txt'
    f = open(reportLocation, "w+")
    f.write("File data: \n")


    print("end of filecheck")
