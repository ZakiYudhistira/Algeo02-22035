import numpy as np
from numpy.linalg import norm
import cv2 as cv
import math as mt
from datasets import load_dataset
import sys

# image processing library

def rgbtoHsv(inputImage : np.ndarray) -> np.ndarray:
    image = inputImage[:,:,[0,1,2]]/255 #standardisasi nilai rgb

    maxValue = np.max(image, axis=2)
    maxValueId = np.argmax(image, axis=2)
    minValue = np.min(image, axis=2)

    deltaValue = maxValue - minValue

    retValue = np.zeros(image.shape, dtype=float)
    retValue[:,:,2] = maxValue
    retValue[:,:,1] = np.where(maxValue == 0, 0, deltaValue/maxValue)
    retValue[:,:,0] = np.where(deltaValue == 0, 0, np.where(maxValueId == 0, ((image[:,:,1]-image[:,:,2])/deltaValue),np.where(maxValueId == 1, ((image[:,:,0]-image[:,:,2])/deltaValue+2), ((image[:,:,0]-image[:,:,1])/deltaValue+4))))
    retValue[:,:,0] = retValue[:,:,0] % 6
    retValue[:,:,0] = retValue[:,:,0]*30
    retValue[:,:,1] = retValue[:,:,1]*255
    retValue[:,:,2] = retValue[:,:,2]*255
    retValue = retValue.astype(int)
    
    return retValue
    

def getSimilarityIndeks(imgInput : np.ndarray, imgQuery : np.ndarray) :
    condition = np.any(imgInput[:,:,:] == [0,0,0] & imgQuery[:,:,:] == [0,0,0])
    dotMatrix = np.where(condition,1,np.sum(imgInput*imgQuery, axis=2))
    normMatrixInput = np.sqrt(np.sum(imgInput**2, axis=2))
    normMatrixInput = np.where(normMatrixInput == 0,1,normMatrixInput)
    normMatrixQuery = np.where(normMatrixQuery == 0,1,normMatrixQuery)
    normMatrixQuery = np.sqrt(np.sum(imgQuery**2, axis=2))
    valueMatrix = dotMatrix/(normMatrixInput*normMatrixQuery)
    return valueMatrix





image = cv.imread("./TestJaki/Test.jpg")
image2 = cv.imread("./TestJaki/Test.jpg")
print(getSimilarityIndeks(image,image2))

# cv.imshow("window",retValue)

# cv.imshow("testing", image)