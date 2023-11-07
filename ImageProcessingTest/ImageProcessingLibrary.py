import numpy as np
from numpy.linalg import norm
import cv2 as cv
import math as mt
import time

# image processing library

def rgbtoHsv(input_image : np.ndarray) -> np.ndarray:
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

    ret_value[:,:,1] = ret_value[:,:,1]*255
    ret_value[:,:,2] = ret_value[:,:,2]*255
    ret_value[:,:,0] = ret_value[:,:,0]*30 
    #Convert to 8 bit format

    ret_value = ret_value.astype(np.uint8) #Cast from float to 8-bit unsigned int
    
    return ret_value
    

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


#Testings
start = time.time()
input_image_PATH = "./ImageProcessingTest/Images/"
output_image_PATH = "./ImageProcessingTest/PostProcessedImages/"

image = cv.imread(input_image_PATH+"Lea.jpg")

new_img = cv.cvtColor(image,cv.COLOR_BGR2HSV)
new_img2 = rgbtoHsv(image)
cv.imwrite(output_image_PATH+"LeaReference.jpg",new_img)
cv.imwrite(output_image_PATH+"LeaResult.jpg",new_img)
end = time.time()
print(end-start)