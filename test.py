import numpy as np
from numpy.linalg import norm
import cv2 as cv2
import math as mt
# from datasets import load_dataset
import sys
# from RetrieveImage import *

# def getCoOccurenceMatrixmini(image : np.ndarray, distance : int, angle : int) -> np.ndarray:
#     retValue = np.zeros((5,5), dtype=int)

#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             if (i+distance < image.shape[0]):
#                 retValue[image[i,j],image[i+distance,j+angle]] += 1
                
#     return retValue

def occurMini(matrix):
    ret = [[0 for j in range(5)] for i in range(5) ]
    for i in range(4):
        for j in range (4):
            if (i + 0 < 4) and (j +1 < 4):
                ret[matrix[i][j]][matrix[i][j+1]] += 1

    return ret

def getCoOccurenceMatrixmini(image : np.ndarray, distance : int) -> np.ndarray:
    retValue = np.zeros((5,5), dtype=int)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if (i< image.shape[0]) and (j+distance < image.shape[1]):
                retValue[image[i,j],image[i,j+distance]] += 1
                
    return retValue

matrix = [[1,2,3,0],
          [2,0,2,4],
          [4,2,3,2],
          [0,1,2,3]]

data = np.array([[1, 2, 3, 0],
                 [2, 0, 2, 4],
                 [4, 2, 3, 2],
                 [0, 1, 2, 3]])
# print(matrix)
print(occurMini(matrix))
print(getCoOccurenceMatrixmini(data,1))
