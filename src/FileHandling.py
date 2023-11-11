import os
from ImageProcessingLibrary import *
from TeksturImg import *
import time

base_path = os.path.dirname(os.path.dirname(__file__))
path_parent =os.path.join(base_path,'test')

def getImagePath(Image):
    element = os.path.join('Upload', Image)
    path_img = os.path.join(path_parent,element)
    return path_img

def getDatasetPath(folder_name):
    path_file = os.path.join(path_parent,folder_name)
    files = os.listdir(path_file)
    # file_path = [os.path.join(path_file,file) for file in files]
    file_Dictionary = {filename : 0 for filename in files}
    return(file_Dictionary)
    
def searchColor(dictionary,folder_name):
    for filename in dictionary.keys():
        path_current = os.path.join(path_parent,folder_name,filename)
        res = runColor(getImagePath('apple.jpg'),path_current)
        dictionary[filename] = res
    new_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return new_dict

def searchTexture(dictionary,folder_name):
    for filename in dictionary.keys():
        path_current = os.path.join(path_parent,folder_name,filename)
        res = runTexture(getImagePath('apple.jpg'),path_current)
        dictionary[filename] = res
    new_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return new_dict
    
start = time.time()
dicti = getDatasetPath('Images')
print(searchColor(dicti,'Images'))
end = time.time()

start1 = time.time()
dicti2 = getDatasetPath('Images')
print(searchTexture(dicti2,'Images'))
end1 = time.time()

print("COLOR")
print(end-start)
print("TEXTURE")
print(end1-start1)