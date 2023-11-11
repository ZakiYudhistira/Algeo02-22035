import numpy as np
from numpy.linalg import norm
import cv2 as cv2
import math as mt
import time
# from datasets import load_dataset
import sys
# from RetrieveImage import *

# CBIR dengan parameter tekstur

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

# Mendapatkan vektor dari CHE, dissimilarity, asm, energy (6 fitur/dimensi)
def getVector(contrast : float, homogeneity : float, entropy : float, dissimilarity : float, asm : float, energy : float) -> np.ndarray:
    vektor = np.array([contrast,homogeneity,entropy,dissimilarity,asm,energy])
    return vektor

# Cosine Similarity
def getSimilarityIndeks(array_input1 : np.array, array_input2 : np.array) -> float:
    dot_result = np.dot(array_input1,array_input2)
    #Retrieve dot product results
    return dot_result/(np.linalg.norm(array_input1)*np.linalg.norm(array_input2))

# Print 256x256 matrix
def print256(image : np.ndarray):
    # Co-Occ matrix : 256x256 NumPy array
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            print(image[i, j], end=' ')  # Printing the pixel value
        print()  # Move to the next line after each row

def run1(image):
    data = getCoOccurenceMatrix(getGrayScaleMatrix(image))
    data = getNormalizedSymmetryMatrix(getSymmetryMatrix(data))
    c = getContrast(data)
    h = getHomogeneity(data)
    e = getEntropy(data)
    v = getVector(c,h,e)
    print(f"Contrast: {c}, Homogeneity: {h}, Entropy: {e}")
    return(v)


# parentPath = "C:/Users/Angelica Gurning/Documents/Kuliah/ALGEO/Tubes_2/Algeo02-22035/test"
start = time.time()

path = "D:/Main Files/File Amel/Kuliah/Akademik/Semester 3/ALGEO/apel.jpg"
path2 = "D:/Main Files/File Amel/Kuliah/Akademik/Semester 3/ALGEO/White.png"

image = cv2.imread(path)
image2 = cv2.imread(path2)
# print(image2)
print(getSimilarityIndeks(run1(image),run1(image2)))

end = time.time()
print(end-start)
# image2 = cv.imread("./TestJaki/joko.jpg")
# print(image)

# newImg = getGrayScaleMatrix(image)
# # print("grayscale")
# # print(newImg)
# print("co-occurence")
# print256(getSymmetryMatrix(getCoOccurenceMatrix(data1,1)))