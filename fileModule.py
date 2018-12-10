import os
import binwalk


def filecheck(input_file, output_folder):
    file_extension = os.path.splitext(input_file)[1][1:]
    fileList = []
    #.jpg first JPEG used to verify between file_extension
    extensionToFile = [('.jpg', 'JPEG'), ('.tif', 'TIFF'), ('.gif', 'GIF'), ('.tif',' TIFF'), ('.tif', 'TIFF')]

    for module in binwalk.scan(input_file, signature=True, quiet=True):
        # print("%s Results:" % module.name)
        for result in module.results:
            print((result.description))
            fileList.append(result.description)

    # matching binwalk filetypes to real filetypes looks like effort (dict/tuples?)
    # current version relies on the quality of people reading it
    reportLocation = output_folder + '/' + 'report.txt'
    f = open(reportLocation, "a+")
    f.write("File data: \n")
    f.write("The os provided extension is " + file_extension + "\n")
    if len(fileList) > 0:
        f.write("Binwalk identified the file as:  " + fileList[0] + "\n")
    else:
        f.write("Binwalk did not identify any magic bytes." + "\n")

    if len(fileList) > 1:
        f.write("Binwalk identified " + str(len(fileList) - 1) + " potential hidden file(s)." + "\n")
        # Needed to skip fileList[0], so this is what happened
        i = 1
        while i < len(fileList):
            f.write("Hidden file " + str(i) + " " + fileList[i] + "\n")
            i += 1

    f.close()
    print("end of filecheck")
