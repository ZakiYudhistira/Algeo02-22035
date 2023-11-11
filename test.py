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
def dissim(matrix):
    dis = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            dis += matrix[i][j] * abs(i-j)
            print(f"[{matrix[i][j]}]")
            print(dis)
    return dis

def getDissimilaritymini(SymmetryMatrix : np.ndarray) -> float:
    retValue = np.sum(SymmetryMatrix*np.abs((np.arange(SymmetryMatrix.shape[0])[:,None]-np.arange(SymmetryMatrix.shape[1]))))
    return retValue


matrix = [[2,2,3,0],
          [2,0,2,4],
          [4,2,6,2],
          [0,10,2,3]]

data = np.array([[2, 2, 3, 0],
                 [2, 0, 2, 4],
                 [4, 2, 6, 2],
                 [0, 10, 2, 3]])
# print(matrix)
print(dissim(matrix))
print(getDissimilaritymini(data))
