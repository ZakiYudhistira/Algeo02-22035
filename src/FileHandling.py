import os
from ImageProcessingLibrary import *
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
    
def getCosineValues(dictionary,folder_name):
    i = 0
    for filename in dictionary.keys():
        path_current = os.path.join(path_parent,folder_name,filename)
        res = searchColor(getImagePath('apple.jpg'),path_current)
        dictionary[filename] = res
    new_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return new_dict


# img = cv.imread(getImagePath('apple.jpg'))
# print(getImagePath('apple.jpg'))
# print("C:\\Users\\Angelica Gurning\\Documents\\Kuliah\\ALGEO\\Tubes_2\\Algeo02-22035\\test\\Upload\\apple.jpg")
# print(img)
# folder_name = "Images"
# pathF = os.path.join(path_parent,folder_name)
# files = os.listdir(pathF)
# print(pathF)
# print("-------------------")
# print("C:\\Users\\Angelica Gurning\\Documents\\Kuliah\\ALGEO\\Tubes_2\\Algeo02-22035\\test\\Images")
# getImagePath('apple.jpg')
dicti = getDatasetPath('Images')
print(getCosineValues(dicti,'Images'))