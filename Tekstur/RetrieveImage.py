import numpy as np
from numpy.linalg import norm
import cv2 as cv
import math as mt
from datasets import load_dataset
import sys

# image processing library

def rgbtoHsv(inputImage : np.ndarray) -> np.ndarray:
    image = inputImage[:,:,[0,1,2]]/255 #standardisasi nilai rgb

    maxValue = np.max(image, axis=2).astype(float)
    maxValueId = np.argmax(image, axis=2)
    minValue = np.min(image, axis=2).astype(float)

    deltaValue = maxValue - minValue
    deltaValue = np.where(deltaValue == 0,1,deltaValue)

    retValue = np.zeros(image.shape, dtype=float)
    mask = maxValue == 0
    retValue[:,:,2] = maxValue
    retValue[:,:,1] = np.divide(deltaValue, maxValue, where=~mask, out=np.zeros_like(deltaValue))
    retValue[:,:,0] = np.where(mask, 0, np.where(maxValueId == 0, ((image[:,:,1]-image[:,:,2])/deltaValue), np.where(maxValueId == 1, ((image[:,:,0]-image[:,:,2])/deltaValue+2), ((image[:,:,0]-image[:,:,1])/deltaValue+4))))
    retValue[:,:,0] = retValue[:,:,0] % 6
    retValue[:,:,0] = retValue[:,:,0]*30
    retValue[:,:,1] = retValue[:,:,1]*255
    retValue[:,:,2] = retValue[:,:,2]*255
    retValue = retValue.astype(int)
    
    return retValue
    

def getSimilarityIndeks(imgInput : np.ndarray, imgQuery : np.ndarray) :
    imgInput = imgInput.astype(int)
    imgQuery = imgQuery.astype(int)
    condition = np.all(imgInput[:,:,:] == [0,0,0]) & np.all(imgQuery[:,:,:] == [0,0,0])
    dotMatrix = np.where(condition,1,np.sum(imgInput*imgQuery, axis=2))
    normMatrixInput = (norm(imgInput, axis=2))
    normMatrixQuery = (norm(imgQuery, axis=2))
    normMatrixInput = np.where(normMatrixInput == 0,1,normMatrixInput)
    normMatrixQuery = np.where(normMatrixQuery == 0,1,normMatrixQuery)
    valueMatrix = dotMatrix/(normMatrixInput*normMatrixQuery)
    return np.average(valueMatrix)





image = cv.imread("./TestJaki/black.png")
image2 = cv.imread("./TestJaki/joko.jpg")

newImg = rgbtoHsv(image2)
cv.imwrite("mas.jpg",newImg)
newImg = cv.cvtColor(image2,cv.COLOR_RGB2HSV)
cv.imwrite("masJoko.jpg",newImg)
# maxValue = np.max(image, axis=2).astype(float)
# maxValueId = np.argmax(image, axis=2)
# minValue = np.min(image, axis=2)
# deltaValue = maxValue - minValue
# deltaValue = np.where(deltaValue == 0, 1,deltaValue)
# retValue = np.zeros(image.shape, dtype=float)
# mask = maxValue == 0
# retValue[:,:,1] = retValue = np.divide(deltaValue, maxValue, where=~mask, out=np.zeros_like(deltaValue))
print(newImg)

# print(getSimilarityIndeks(image,image2))
# print(np.all(image[1,2,:] == [122,136,225]) & np.all(image[1,2,:]==[0,0,0]))
# print(image)
# print(image2)
# print(getSimilarityIndeks(image,image2))
# print(np.all(np.array([True,False,True])))

# cv.imshow("window",retValue)

# cv.imshow("testing", image)