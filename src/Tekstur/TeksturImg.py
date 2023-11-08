import numpy as np
from numpy.linalg import norm
import cv2 as cv
import math as mt
from datasets import load_dataset
import sys
from RetrieveImage import *

# CBIR dengan parameter tekstur

# Matriks Co-Occurence
def getCoOccurenceMatrix(image : np.ndarray, distance : int, angle : int) -> np.ndarray:
    image = image.astype(int)
    retValue = np.zeros((256,256), dtype=int)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if (i+distance < image.shape[0]) and (j+angle < image.shape[1]):
                retValue[image[i,j],image[i+distance,j+angle]] += 1
    return retValue

# Matriks RGB to Gray scale
def getGrayScaleMatrix(image : np.ndarray) -> np.ndarray:
    # retValue[i,j] = (0.29*image[i,j,0]+0.587*image[i,j,1]+0.114*image[i,j,2])
    retValue = np.zeros((image.shape[0],image.shape[1]), dtype=int)
    retValue[:,:,0] = (0.29*image[:,:,0]+0.587*image[:,:,1]+0.114*image[:,:,2])
    return retValue

# Matriks Normalisasi
def getNormalizedCoOccurenceMatrix(coOccurence_matrix : np.ndarray) -> np.ndarray:
    retValue = coOccurence_matrix.astype(float)
    retValue = retValue/np.sum(retValue)
    return retValue

# Matriks Kontras
def getContrast(coOccurence_matrix : np.ndarray) -> float:
    retValue = np.sum(coOccurence_matrix*(np.arange(coOccurence_matrix.shape[0])[:,None]-np.arange(coOccurence_matrix.shape[1]))**2)
    return retValue

# Matriks Homogenitas
def getHomogeneity(coOccurence_matrix : np.ndarray) -> float:
    retValue = np.sum(coOccurence_matrix/(1+(np.arange(coOccurence_matrix.shape[0])[:,None]-np.arange(coOccurence_matrix.shape[1]))**2))
    return retValue

# Matriks Entropi
def getEntropy(coOccurence_matrix : np.ndarray) -> float:
    retValue = np.sum(coOccurence_matrix*np.log10(coOccurence_matrix))
    return -retValue

image = cv.imread("./TestJaki/black.png")
image2 = cv.imread("./TestJaki/joko.jpg")

newImg = getCoOccurenceMatrix(image2,1,0)
print(newImg)