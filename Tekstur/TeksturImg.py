import numpy as np
from numpy.linalg import norm
import cv2 as cv
import math as mt
from datasets import load_dataset
import sys
import TestJaki.RetrieveImage as ri

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

# Matriks Normalisasi
def getNormalizedCoOccurenceMatrix(coOccurenceMatrix : np.ndarray) -> np.ndarray:
    retValue = coOccurenceMatrix.astype(float)
    retValue = retValue/np.sum(retValue)
    return retValue

# Matriks Kontras
def getContrast(coOccurenceMatrix : np.ndarray) -> float:
    retValue = 0
    for i in range(coOccurenceMatrix.shape[0]):
        for j in range(coOccurenceMatrix.shape[1]):
            retValue += (i-j)**2 * coOccurenceMatrix[i,j]
    return retValue

# Matriks Homogenitas
def getHomogeneity(coOccurenceMatrix : np.ndarray) -> float:
    retValue = 0
    for i in range(coOccurenceMatrix.shape[0]):
        for j in range(coOccurenceMatrix.shape[1]):
            retValue += coOccurenceMatrix[i,j]/(1+abs(i-j))
    return retValue

# Matriks Entropi
def getEntropy(coOccurenceMatrix : np.ndarray) -> float:
    retValue = 0
    for i in range(coOccurenceMatrix.shape[0]):
        for j in range(coOccurenceMatrix.shape[1]):
            if coOccurenceMatrix[i,j] != 0:
                retValue += coOccurenceMatrix[i,j]*mt.log(coOccurenceMatrix[i,j])
    return -retValue

image = cv.imread("./TestJaki/black.png")
image2 = cv.imread("./TestJaki/joko.jpg")

newImg = ri.rgbtoHsv(image2)
print(newImg)