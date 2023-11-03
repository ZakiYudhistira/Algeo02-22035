import numpy as np
import cv2 as cv
import math as mt
import sys

def rgbtoHsv(image : np.ndarray) -> np.ndarray:
    retValue = image[:,:,[0,1,2]]/255 #standardisasi nilai rgb

    maxValue = np.max(image, axis=2)
    maxValueId = np.argmax(image, axis=2)
    minValue = np.min(image, axis=2)
    minValueId = np.argmin(image, id=2)

    deltaValue = maxValue - minValue

    retValue = np.zeros(image.shape, dtype=float)
    retValue[:,:,2] = maxValue
    retValue[:,:,1] = np.where(maxValue == 0, 0, deltaValue/maxValue)
    retValue[:,:,0] = np.where(deltaValue == 0, 0, np.where(maxValueId == 2, ((image[:,:,1]-image[:,:,0])/deltaValue),np.where(maxValueId == 1, ((image[:,:,0]-image[:,:,2])/deltaValue+2), ((image[:,:,2]-image[:,:,1])/deltaValue+4))))
    retValue[:,:,0] = retValue[:,:,0] % 6
    retValue[:,:,0] = retValue[:,:,0]*30
    retValue[:,:,1] = retValue[:,:,1]*255
    retValue[:,:,2] = retValue[:,:,2]*255
    retValue = retValue.astype(int)
    
    return retValue
    


image = cv.imread("./TestJaki/Test.jpg")
compare = cv.cvtColor(image,cv.COLOR_RGB2HSV)
print(image)
print("===")
image = image[:,:,[0,1,2]]/255 #standardisasi nilai rgb

maxValue = np.max(image, axis=2)
maxValueId = np.argmax(image, axis=2)
minValue = np.min(image, axis=2)
minValueId = np.argmin(image, axis=2)
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


deltaValue = maxValue - minValue
cv.imwrite("ganteng.jpeg",retValue)
cv.imwrite("ganteng2.jpeg",compare)
print(retValue)
print("====")
print(compare)

# cv.imshow("window",retValue)

# cv.imshow("testing", image)
cv.waitKey(0)
cv.destroyAllWindows()