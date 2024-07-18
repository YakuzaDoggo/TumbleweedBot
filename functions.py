# Before using this code for any reason (running, editing) please read the license included in the LICENSE folder

import sys
import os
from os.path import isfile, join
from random import randint
sys.path.insert(0, './images/')
import pathlib
import images

# Array that sifts through the images folder located in ./images/ to add them to an array
# ran at start of the bot
def UpdateArray():
    directory = pathlib.Path('./images/images')
    for currentFile in directory.iterdir():
        images.images.append(currentFile)
