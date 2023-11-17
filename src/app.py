from flask import Flask, render_template,request,jsonify,send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from ImageProcessingLibrary import *
import logging,os,time,multiprocessing
import numpy as np
import pandas as pd
import cv2 as cv

app = Flask(__name__)
CORS(app)
app.logger.setLevel(logging.DEBUG)

imagepath =""
imageVectorColor = None
imageVectorTexture = None

#  Path Image, Dataset, and Download Folder
base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"src","my-app","public")
UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")

def writeCache():
    main = np.zeros(126)
    for filename in os.listdir(UPLOAD_DATASET):
        img = cv.imread(os.path.join(UPLOAD_DATASET,filename))
        img = normBGRtoHSV(img)
        img = get3X3Histograms(img)
        main = np.vstack((main,img))
    main = np.delete(main,0,0)
    data = pd.DataFrame(main)
    data.to_csv(os.path.join(UPLOAD_DATASET,"cache.csv"), header=False, index=False)

def getCache():
    if(os.path.exists(os.path.join(UPLOAD_DATASET,"cache.csv"))):
        data = np.loadtxt(open(os.path.join(UPLOAD_DATASET,"cache.csv"), "rb"), delimiter=",", dtype=int)
        return data
    else:
        writeCache()
        try:
            data = np.loadtxt(open(os.path.join(UPLOAD_DATASET,"cache.csv"), "rb"), delimiter=",", dtype=int)
            return data
        except:
            app.logger.debug("Failed to cache dataset")
            
def searchColor():
    data = []
    for filename in os.listdir(UPLOAD_DATASET):
        pathAbs = os.path.join(UPLOAD_DATASET, filename)
        path_current = "/Dataset/" + filename
        res = getSimilarityIndeks(imageVectorColor,getVectorColor(pathAbs))
        if res > 0.6:
            data.append({"path": path_current, "value": round(res*100,2)})
    sorted_data = sorted(data, key=lambda x: x["value"], reverse=True)
    return sorted_data

def getVectorColor(path):
    img = cv.imread(path)
    img = normBGRtoHSV(img)
    return get3X3Histograms(img)

def searchTexture():
    data = []
    for filename in os.listdir(UPLOAD_DATASET):
        pathAbs = os.path.join(UPLOAD_DATASET, filename)
        path_current = "/Dataset/" + filename
        res = getSimilarityIndeks(imageVectorTexture,getVectorTexture(pathAbs))
        if res > 0.6:
            data.append({"path": path_current, "value": round(res*100,2)})
    sorted_data = sorted(data, key=lambda x: x["value"], reverse=True)
    return sorted_data

# def searchTexture():
#     data = []
#     for filename in os.listdir(UPLOAD_DATASET):
#         pathAbs = os.path.join(UPLOAD_DATASET, filename)
#         path_current = "/Dataset/" + filename
#         res = runTexture(imagepath, pathAbs)
#         if res > 0.6:
#             data.append({"path": path_current, "value": round(res*100,2)})
#     sorted_data = sorted(data, key=lambda x: x["value"], reverse=True)
#     return sorted_data


# Function to return the similarity index in on go (COLOR)
# def runColor(image1,image2):
#     img1 = cv.imread(image1)
#     img1 = normBGRtoHSV(img1)
#     img2 = cv.imread(image2)
#     img2 = normBGRtoHSV(img2)
#     return(getSimilarityIndeks(get3X3Histograms(img1),get3X3Histograms(img2)))

# Function to process the image in one go
def getVectorTexture(path):
    img1 = cv.imread(path)
    data = getCoOccurenceMatrix(getGrayScaleMatrix(img1))
    data = getNormalizedSymmetryMatrix(getSymmetryMatrix(data))

    with multiprocessing.Pool() as pool:
        features = pool.map(extractFeature, [(data, func) for func in [getContrast, getHomogeneity, getEntropy, getASM, getEnergy, getDissimilarity]])

    v = getVector(*features)
    return v

def extractFeature(args):
    data, func = args
    return func(data)

# Function to return the similarity index in on go (Texture)
# def  runTexture(image1,image2):
#     img1 = cv.imread(image1)
#     img2 = cv.imread(image2)
#     img1 = processTexture(img1)
#     img2 = processTexture(img2)
#     return (getSimilarityIndeks(img1,img2))

# Post an image to Upload folder and a folder of images to Dataset folder
@app.route('/api/upload', methods=['POST'])
def upload():
    global imagepath, imageVectorColor, imageVectorTexture
    try:
        if not os.path.isdir(base_path):
            os.mkdir(base_path)

        if 'image' in request.files:
            imagepath = ""
            if not os.path.isdir(UPLOAD_IMAGE):
                os.mkdir(UPLOAD_IMAGE)
            image = request.files['image']
            filename = secure_filename(image.filename)
            path = os.path.join(UPLOAD_IMAGE, filename)
            imagepath = path
            files = os.listdir(UPLOAD_IMAGE)
            if files:
                for file in files:
                    os.remove(os.path.join(UPLOAD_IMAGE, file))
            image.save(path)
            imageVectorColor = getVectorColor(path)
            imageVectorTexture = getVectorTexture(path)
            return jsonify({"message": "File uploaded successfully"})
        elif 'dataset' in request.files:
            if not os.path.isdir(UPLOAD_DATASET):
                os.mkdir(UPLOAD_DATASET)
            dataset_files = request.files.getlist('dataset')
            files = os.listdir(UPLOAD_DATASET)
            if files:
                for file in files:
                    os.remove(os.path.join(UPLOAD_DATASET, file))
            for dataset in dataset_files:
                dataset_name = secure_filename(dataset.filename)
                dataset_path = os.path.join(UPLOAD_DATASET, dataset_name)
                dataset.save(dataset_path)
            return jsonify({"message": "Dataset uploaded successfully"})
        return jsonify({"error": "No file provided"}, 400)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
# Endpoint for using the CBIR functions
@app.route('/api/cbir', methods=['POST', 'GET'])
def run():
    app.logger.debug('Received a request to /api/cbir')
    try:
        if request.method == 'POST':
            option = request.json.get('option')
            if option == 'color':
                app.logger.debug('Color method found in request')
                start_time = time.time()
                result = searchColor()
            elif option == 'texture':
                app.logger.debug('Texture method found in request')
                start_time = time.time()
                result = searchTexture()
            else:
                return jsonify({"error": "Invalid option"}), 400

            end_time = time.time()
            delta_time = end_time - start_time
            
            return jsonify({"result": result, "delta_time" : delta_time})

        return jsonify({"error": "No method provided"}, 400)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
# Endpoint for downloading the result
# @app.route('/api/download', methods=['POST'])
# def download():
#     app.logger.debug('Received a request to /api/download')
#     try:
#         if not os.path.isdir(DOWNLOAD_FOLDER):
#             os.mkdir(DOWNLOAD_FOLDER)
#         if request.form['method'] == 'color':
#             app.logger.debug('Color method found in request')
#             result = searchColor()
#             return jsonify(result)
#         elif request.form['method'] == 'texture':
#             app.logger.debug('Texture method found in request')
#             result = searchTexture()
#             return jsonify(result)
#         return jsonify({"error": "No method provided"}, 400)
#     except Exception as e:
#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
# Endpoint for downloading the result
# @app.route('/api/download/<path:filename>', methods=['GET', 'POST'])
# def download_file(filename):
#     app.logger.debug('Received a request to /api/download/<path:filename>')
#     try:
#         return send_from_directory(DOWNLOAD_FOLDER, filename=filename, as_attachment=True)
#     except Exception as e:
#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)