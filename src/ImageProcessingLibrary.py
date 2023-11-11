import numpy as np
import cv2 as cv
import time

# image processing library

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

def runColor(image1,image2):
        img1 = cv.imread(image1)
        img1 = normBGRtoHSV(img1)
        img2 = cv.imread(image2)
        img2 = normBGRtoHSV(img2)
        return(getSimilarityIndeks(get3X3Histograms(img1),get3X3Histograms(img2)))

#Testings
start = time.time()
input_image_PATH = "./test/Images/"
output_image_PATH = "./ImageProcessingTest/PostProcessedImages/"

image1 = cv.imread(input_image_PATH+"Lea.jpg")

# image2 = cv.imread(input_image_PATH+"Lea.jpg")
new_img1 = normBGRtoHSV(image1)
# new_img2 = normBGRtoHSV(image2)
# hue_hist[7] += hue_hist[0]
# hue_hist = np.delete(hue_hist,0)

# print(hue_bins)
# new_img2 = cv.rotate(image1, cv.ROTATE_180)
#Validity checking

print(get3X3Histograms(new_img1))
# print("%.2f"%getSimilarityIndeks(get3X3Histograms(new_img1),get3X3Histograms(new_img2)))

# end = time.time()
# print(end-start)
