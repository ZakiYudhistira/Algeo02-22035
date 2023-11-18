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

# start = time.time()
# print(searchColor())
# end = time.time()
# print(end-start)

# path ="C:\\Users\\Angelica Gurning\\Documents\\Kuliah\\ALGEO\\Tubes_2\\Algeo02-22035\\src\\my-app\\public\\Upload\\Image20231116022159.jpg"
# imageVector = getImageVectorColor(path)
# print(getSimilarityIndeks(imageVector,imageVector))


# def getCacheColor():
#     cache_file_path = os.path.join(CACHING_FOLDER, "color_cache.csv")

#     if os.path.exists(cache_file_path):
#         # Load data from CSV using pandas
#         data = pd.read_csv(cache_file_path, index_col='filename', converters={'vectors': eval}) 
#         cache = {"filenames": data.index.tolist(), "vectors": data['vectors'].tolist()}
#         return cache
#     else:
#         return {"filenames": [], "vectors": []}
    

# def getCache(csv_path):
#     df = pd.read_csv(csv_path, header=None, names=['filename', 'vector'])
#     df['vector'] = df['vector'].apply(ast.literal_eval)  # Convert string representation to a list
#     data_dict = df.set_index('filename')['vector'].to_dict()
#     return data_dict

# writeCacheColor()
# print(cacheColor)




# imgvector = getVectorColor("C:\\Users\\Angelica Gurning\\Documents\\Kuliah\\ALGEO\\Tubes_2\\Algeo02-22035\\src\\my-app\\public\\Upload\\Image20231116022159.jpg")
# def searchColor_Cache():
#     data = []
#     for key in cacheColor.keys():
#         path_current = "/Dataset/" + key
#         res = getSimilarityIndeks(imgvector,cacheColor[key])
#         if res > 0.6:
#             data.append({"path": path_current, "value": round(res*100,2)})
#     sorted_data = sorted(data, key=lambda x: x["value"], reverse=True)
#     return sorted_data
# writeCacheColor()
# imageVectorColor = getVectorColor("C:\\Users\\Angelica Gurning\\Documents\\Kuliah\\ALGEO\\Tubes_2\\Algeo02-22035\\src\\my-app\\public\\Upload\\Image20231116022159.jpg")
# print(searchColorCache())

relPath = "/Dataset/aa"
a = os.path.basename(relPath)
print(a)