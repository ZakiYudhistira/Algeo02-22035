import os
import time
import numpy as np
import cv2 as cv


# ------- CONTENT BASED IMAGE RETRIEVAL : COLOR -------

def normBGRtoHSV(input_image : np.ndarray) -> np.ndarray:
    image = input_image[:,:,[0,1,2]]/255 #Image standardization

    max_value = np.max(image, axis=2).astype(float)
    max_value_id = np.argmax(image, axis=2)
    min_value = np.min(image, axis=2).astype(float)
    delta_value = max_value - min_value
    #Max, Min, and DeltaValue initiation

    ret_value = np.zeros(image.shape, dtype=float)
    mask = max_value == 0
    ret_value[:,:,2] = max_value #Value assignment
    ret_value[:,:,1] = np.divide(delta_value, max_value, where=~mask, out=np.zeros_like(delta_value)) #Saturation assignment
    delta_value = np.where(delta_value == 0,1,delta_value)
    ret_value[:,:,0] = np.where(mask, 0, np.where(max_value_id == 0, ((image[:,:,1]-image[:,:,2])/delta_value+4), np.where(max_value_id == 1, ((image[:,:,0]-image[:,:,2])/delta_value+2), ((image[:,:,0]-image[:,:,1])/delta_value)))) #Hue assignment
    ret_value[:,:,0] = ret_value[:,:,0] % 6 #Hue value correction to match 360 degrees

    ret_value[:,:,1] = ret_value[:,:,1]*100
    ret_value[:,:,2] = ret_value[:,:,2]*100
    ret_value[:,:,0] = ret_value[:,:,0]*60 
    #Convert to standard format

    ret_value = ret_value.astype(int) #Cast from float to int
    
    return ret_value

def splitChannels(input_image : np.ndarray) -> tuple[np.array, np.array, np.array]:
    hue_values = input_image[:,:,0].flatten()
    saturation_values = input_image[:,:,1].flatten()
    values_values = input_image[:,:,2].flatten()
    #split hue, saturation, and values channel
    return hue_values,saturation_values,values_values

def getHistogram(input_image : np.ndarray) -> np.array:
    hue_values,saturation_values,values_values = splitChannels(input_image)
    #Retrieve hue, saturation, and values array

    histogram_hue,_ = np.histogram(hue_values,bins=[0,26,41,121,191,271,296,316,360])
    histogram_saturation,_ = np.histogram(saturation_values,bins=[0,20,70,100])
    histogram_values,_ = np.histogram(values_values,bins=[0,20,70,100])
    #Retrieve hue, saturation, and values histograms' count

    return np.hstack((histogram_hue,histogram_saturation,histogram_values))
    #Return global histogram array for cosine similarity calculation

def getSimilarityIndeks(array_input1 : np.array, array_input2 : np.array) -> float:
    dot_result = np.dot(array_input1,array_input2)
    #Retrieve dot product results
    return dot_result/(np.linalg.norm(array_input1)*np.linalg.norm(array_input2))
    #Normalize dot product value

def get3X3Histograms(input_image : np.ndarray) -> np.array:
    seg1,seg2,seg3,seg4,seg5,seg6,seg7,seg8,seg9 = get3X3Segments(input_image)
    hist_seg1 = getHistogram(seg1)
    hist_seg2 = getHistogram(seg2)
    hist_seg3 = getHistogram(seg3)
    hist_seg4 = getHistogram(seg4)
    hist_seg5 = getHistogram(seg5)
    hist_seg6 = getHistogram(seg6)
    hist_seg7 = getHistogram(seg7)
    hist_seg8 = getHistogram(seg8)
    hist_seg9 = getHistogram(seg9)
    #calculate each histogram for 9 segments
    return np.hstack((hist_seg1,hist_seg2,hist_seg3,hist_seg4,hist_seg5,hist_seg6,hist_seg7,hist_seg8,hist_seg9))

def get3X3Segments(input_array : np.ndarray) -> tuple:
    height,width,_ = input_array.shape
    #Retrieve height, width, and depth(not necessary)
    if(height < 3 or width < 3):
        return (), (), (), (), (), (), (), (), ()
        #if unable to divide
    else:
        height1 = height // 3
        height2 = height1 * 2

        width1 = width // 3
        width2 = width1 * 2

        ret11 = input_array[:height1, :width1,:]
        ret12 = input_array[:height1, width1:width2,:]
        ret13 = input_array[:height1, width2:,:]
        ret21 = input_array[height1:height2, :width1,:]
        ret22 = input_array[height1:height2, width1:width2,:]
        ret23 = input_array[height1:height2, width2:,:]
        ret31 = input_array[height2:, :width1,:]
        ret32 = input_array[height2:, width1:width2,:]
        ret33 = input_array[height2:, width2:,:]

    return ret11,ret12,ret13,ret21,ret22,ret23,ret31,ret32,ret33
    #return all divided images

# Function to return the similarity index in on go (COLOR)
def runColor(image1,image2):
    img1 = cv.imread(image1)
    img1 = normBGRtoHSV(img1)
    img2 = cv.imread(image2)
    img2 = normBGRtoHSV(img2)
    return(getSimilarityIndeks(get3X3Histograms(img1),get3X3Histograms(img2)))


# ------- CONTENT BASED IMAGE RETRIEVAL : TEXTURE -------

# Matriks BGR to Gray scale
def getGrayScaleMatrix(image : np.ndarray) -> np.ndarray:
    retValue = np.zeros((image.shape[0],image.shape[1]), dtype=int)
    retValue = (0.29*image[:,:,2]+0.587*image[:,:,1]+0.114*image[:,:,0])
    return retValue.astype(int)

# Matriks Co-Occurence, distance = 1, angle = 0
def getCoOccurenceMatrix(image : np.ndarray) -> np.ndarray:
    retValue = np.zeros((256,256), dtype=int)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if (i< image.shape[0]) and (j+1 < image.shape[1]):
                retValue[image[i,j],image[i,j+1]] += 1
                
    return retValue

# Matriks Symmetry
def getSymmetryMatrix(coOccurence_matrix: np.ndarray) -> np.ndarray:
    retValue = np.add(coOccurence_matrix, np.transpose(coOccurence_matrix))
    return retValue

# Matriks Normalisasi
def getNormalizedSymmetryMatrix(SymmetryMatrix : np.ndarray) -> np.ndarray:
    retValue = SymmetryMatrix.astype(float)
    retValue = retValue/np.sum(retValue)
    return retValue

# Matriks Kontras
def getContrast(SymmetryMatrix : np.ndarray) -> float:
    retValue = np.sum(SymmetryMatrix*(np.arange(SymmetryMatrix.shape[0])[:,None]-np.arange(SymmetryMatrix.shape[1]))**2)
    return retValue

# Matriks Homogenitas
def getHomogeneity(SymmetryMatrix : np.ndarray) -> float:
    retValue = np.sum(SymmetryMatrix/(1+(np.arange(SymmetryMatrix.shape[0])[:,None]-np.arange(SymmetryMatrix.shape[1]))**2))
    return retValue

# Matriks Entropi
def getEntropy(SymmetryMatrix : np.ndarray) -> float:
    # handling jika elemen matriks = 0
    valid_values = SymmetryMatrix[SymmetryMatrix > 0]
    retValue = np.sum(-1*valid_values*np.log10(valid_values))
    return retValue

# Matriks Angular Second Moment (ASM)
def getASM(SymmetryMatrix : np.ndarray) -> float:
    retValue = np.sum(SymmetryMatrix**2)
    return retValue

# Matriks Energy
def getEnergy(SymmetryMatrix : np.ndarray) -> float:
    retValue = np.sqrt(getASM(SymmetryMatrix))
    return retValue

# Matriks disimmilarity
def getDissimilarity(SymmetryMatrix : np.ndarray) -> float:
    retValue = np.sum(SymmetryMatrix*np.abs((np.arange(SymmetryMatrix.shape[0])[:,None]-np.arange(SymmetryMatrix.shape[1]))))
    return retValue

# Mendapatkan vektor dari CHE, dissimilarity, asm, energy (6 fitur/dimensi)
def getVector(contrast : float, homogeneity : float, entropy : float, dissimilarity : float, asm : float, energy : float) -> np.ndarray:
    vektor = np.array([contrast,homogeneity,entropy,dissimilarity,asm,energy])
    return vektor

# Function to process the image in one go
def processTexture(image):
    data = getCoOccurenceMatrix(getGrayScaleMatrix(image))
    data = getNormalizedSymmetryMatrix(getSymmetryMatrix(data))
    c = getContrast(data)
    h = getHomogeneity(data)
    e = getEntropy(data)
    asm = getASM(data)
    d = getDissimilarity(data)
    energy = getEnergy(data)
    v = getVector(c,h,e,d,asm,energy)
    return(v)

# Function to return the similarity index in on go (Texture)
def  runTexture(image1,image2):
    img1 = cv.imread(image1)
    img2 = cv.imread(image2)
    img1 = processTexture(img1)
    img2 = processTexture(img2)
    return (getSimilarityIndeks(img1,img2))

# ------- FILE HANDLING -------

#  Path Image, Dataset, and Download Folder
base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"src","my-app","public")
UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")

# global img 
# img =""
# #  Function to get the path of the image
# def getImagePath():
#     global img
#     img = ""
#     img_files = os.listdir(UPLOAD_IMAGE)
#     if img_files:
#         img = os.path.join("..","public","Dataset",img_files[0])
#         return img
#     else:
#         return None



#  Function to return CBIR color result
# def searchColorn():
#     list = []
#     for filename in os.listdir(UPLOAD_DATASET):
#         dictionary = {}
#         path_current = os.path.join(UPLOAD_DATASET,filename)
#         res = runColor(getImagePath(),path_current)
#         if res > 0.6:
#             dictionary["path"] = filename
#             dictionary["cosine"] = round(res * 100, 2)
#             list.append(dictionary)
#     return sorted(list,key=lambda x: x['cosine'], reverse=True)

# #  Function to return CBIR texture result
# def searchTexturen():
#     list = []
#     for filename in os.listdir(UPLOAD_DATASET):
#         dictionary = {}
#         path_current = os.path.join(UPLOAD_DATASET,filename)
#         res = runTexture(getImagePath(),path_current)
#         if res > 0.6:
#             dictionary["path"] = filename
#             dictionary["cosine"] = round(res * 100, 2)
#             list.append(dictionary)
#     return sorted(list,key=lambda x: x['cosine'], reverse=True)

# def searchColorTuples():
#     list = []
#     for filename in os.listdir(UPLOAD_DATASET):
#         path_current = os.path.join(UPLOAD_DATASET,filename)
#         res = runColor(getImagePath(),path_current)
#         if res > 0.6:
#             list.append((path_current,round(res * 100, 2)))
#     return sorted(list, key=lambda item: item[1], reverse=True)

# print(getImagePath())