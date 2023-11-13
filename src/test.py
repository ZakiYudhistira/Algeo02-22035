# ---------- FILE FOR TESTINGS -----------
from ImageProcessingLibrary import *
import time

#Testings
# start = time.time()
# input_image_PATH = "./test/Images/"
# output_image_PATH = "./ImageProcessingTest/PostProcessedImages/"

# image1 = cv.imread(input_image_PATH+"Lea.jpg")

# image2 = cv.imread(input_image_PATH+"Lea.jpg")
# new_img1 = normBGRtoHSV(image1)
# new_img2 = normBGRtoHSV(image2)
# hue_hist[7] += hue_hist[0]
# hue_hist = np.delete(hue_hist,0)

# print(hue_bins)
# new_img2 = cv.rotate(image1, cv.ROTATE_180)
#Validity checking

# print(get3X3Histograms(new_img1))
# print("%.2f"%getSimilarityIndeks(get3X3Histograms(new_img1),get3X3Histograms(new_img2)))

# end = time.time()
# print(end-start)


# start = time.time()
# dicti = getDatasetPath('Images')
# print(searchColor(dicti,'Images'))
# print(searchTexture())
# end = time.time()
# print(getDatasetPath())
# start1 = time.time()
# dicti2 = getDatasetPath('Images')
# print(searchTexture(dicti2,'Images'))
# end1 = time.time()

# print("COLOR")
# print(end-start)
# print("TEXTURE")
# print(end1-start1)

# searchColor()
# import os

# # Read an image from file
# image = cv.imread(getImagePath('mark.jpeg'))

# # Check if the image was successfully loaded
# if image is not None:
#     # Specify the output folder
#     output_folder = os.path.join(path_parent,'Dataset')

#     # Ensure the output folder exists, create it if necessary
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Construct the full path for the output image
#     output_path = os.path.join(output_folder, 'output_image.jpg')
#     newimg = getGrayScaleMatrix(image)
#     # Write the image to the specified folder
#     cv.imwrite(output_path, newimg)
#     print(f'Image successfully written to {output_path}.')
# else:
#     print('Error: Could not load the image.')


# for filename in dictionary.keys():
#     path_current = os.path.join(UPLOAD_DATASET,filename)
#     res = runColor(getImagePath(),path_current)
#     dictionary[filename] = res

# new_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

# searchColor()
# start = time.time()
# print(searchColor())
# end = time.time()
# print(end-start)
