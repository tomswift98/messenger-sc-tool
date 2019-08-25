#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# imports
from PIL import Image
import os, sys


# check for windoze
if os.name == 'nt':
   print('error: this probably doesnt work on windows')
   exit()


# source messenger screenshot locations
root_path = os.getcwd() + "/" 
# source_path = root_path + sys.argv[1] + "/"
source_path = root_path + "/cropme/"


# make sure folders exist where they should
try:
    os.stat(source_path)
except:
    print('error: source directory not found, exiting')
    exit()
try:
    os.stat(root_path + 'cropped/')
except:
    os.mkdir(root_path + 'cropped/')

try:
    os.stat(root_path + 'archive/')
except:
    os.mkdir(root_path + 'archive/')

try:
    os.stat(root_path + 'downloaded/')
except:
    os.mkdir(root_path + 'downloaded/')


# crop method
def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)


# main loop
for filename in os.listdir(source_path):

    image = source_path + filename
    
    if filename[:3] == "rtc": # if image is a screenshot
        print(image) # useful for debugging

        # this line will need to change based on image resolution
        # currently just takes left half of image, moves to cropped 
        crop(image, (0, 0, 384, 640), root_path + 'cropped/' + filename)
       
        # moves original to archive
        os.rename(image, root_path+'archive/'+filename) 

    else: # image must be saved from a chat
        # moves image to download folder
        os.rename(image, root_path+'downloaded/'+filename)
