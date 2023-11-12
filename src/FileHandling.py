import os
from ImageProcessingLibrary import *
import time
import cv2 as cv

base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"test")
UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")


base_path = os.path.dirname(os.path.dirname(__file__))
path_parent =os.path.join(base_path,'test')

def getImagePath():
    img = os.listdir(UPLOAD_IMAGE)
    path_img = os.path.join(UPLOAD_IMAGE,img[0])
    return path_img

def getDatasetPath():
    files = os.listdir(UPLOAD_DATASET)
    file_Dictionary = {filename : 0 for filename in files}
    return file_Dictionary
    
def searchColor():
    dictionary = getDatasetPath()
    for filename in dictionary.keys():
        path_current = os.path.join(UPLOAD_DATASET,filename)
        res = runColor(getImagePath(),path_current)
        dictionary[filename] = res
    new_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return new_dict

def searchTexture():
    dictionary = getDatasetPath()
    for filename in dictionary.keys():
        path_current = os.path.join(UPLOAD_DATASET,filename)
        res = runTexture(getImagePath(),path_current)
        dictionary[filename] = res
    new_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return new_dict
    
