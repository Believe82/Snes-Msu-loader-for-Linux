import os
import sys
import subprocess
from subprocess import Popen

def choose_option(choice):
    #creates the menu and allows the user to choose
    menu = {index: value for index,
            value in enumerate(choice, start = 1)}
    selection = 0
    
    while selection == 0:
        options = menu.keys()
        
        for entry in options:
            print(entry, menu[entry])

        selection = int(input("Please Select:"))

        if selection in options:
            break

        else:
            print("Unknown Option Selected!")
            selection = 0

    return menu[selection]


def back_insert(filename):
    #inserts backslashes into paths that have spaces in them
    flist = list(filename)
    i = 0
    
    while i < len(flist):
        if flist == " ":
            flist.insert(i, "\\")
            i += 2

        else: i += 1

    fstring = "".join(flist)

    return fstring


#sets the Download path
dpath = back_insert("/home/user/Downloads/")

#sets the Msu path
spath = back_insert(".../snes/msu/")

#creates a list with all the files in Download folder
files = [f for f in os.listdir(dpath) if f.endswith(".sfc")]

#determines which filename to be used
if len(files) < 1:
    print("Error: no rom files in Dowload dir")
    sys.exit()

elif len(files) == 1:
    fchoice = back_insert(files[0])

else:
    fchoice = back_insert(choose_option(files))

#creates a list with all the directories in Msu Folder
subfolders = [f.name for f in os.scandir(spath) if f.is_dir()]

#Chooses the Msu
if len(subfolders) < 1:
    print("Error: no folders in your msu directory")
    sys.exit()

elif len(subfolders) == 1:
    schoice = back_insert(subfolders[0])

else:
    schoice = back_insert(choose_option(subfolders))

#Renames the file and moves it to the Msu folder
move = ("mv " + dpath + fchoice + " " + spath + schoice +
        "/" + schoice + ".sfc")
subprocess.call(move, shell = True)

#Runs the Emulator, socket, Timer and Tracker
#Edit your paths here, Delete a line if you dont want to load a program
commands = [
back_insert("/usr/bin/snes9x-gtk"),                 #Emulator
back_insert("/usr/share/OpenTracker/OpenTracker"),  #Tracker
back_insert("/usr/bin/QUsb2Snes"),                  #Wsocket
back_insert("/home/user/LibreSplit/libresplit")     #Timer
]

procs = [Popen(i) for i in commands]
for p in procs:
    p.wait()
