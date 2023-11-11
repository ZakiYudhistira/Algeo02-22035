import os
from ImageProcessingLibrary import *
import time
import cv2 as cv

base_path = os.path.dirname(os.path.dirname(__file__))
path_parent =os.path.join(base_path,'test')

def getImagePath(Image):
    element = os.path.join('Upload', Image)
    path_img = os.path.join(path_parent,element)
    return path_img

def getDatasetPath(folder_name):
    path_file = os.path.join(path_parent,folder_name)
    files = os.listdir(path_file)
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


# import os

# # Read an image from file
# image = cv.imread(getImagePath('mark.jpeg'))

# # Check if the image was successfully loaded
# if image is not None:
#     # Specify the output folder
#     output_folder = os.path.join(path_parent,'Dataset')

#     # Ensure the output folder exists, create it if necessary
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Construct the full path for the output image
#     output_path = os.path.join(output_folder, 'output_image.jpg')
#     newimg = getGrayScaleMatrix(image)
#     # Write the image to the specified folder
#     cv.imwrite(output_path, newimg)
#     print(f'Image successfully written to {output_path}.')
# else:
#     print('Error: Could not load the image.')