import sys
import os
from os.path import isfile, join
from random import randint
sys.path.insert(0, './images/')
import pathlib
import images

def UpdateArray():
    directory = pathlib.Path('./images/images')
    for currentFile in directory.iterdir():
        images.images.append(currentFile)
