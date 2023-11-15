from flask import Flask, render_template,request,jsonify,send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from ImageProcessingLibrary import *
from io import BytesIO
from PIL import Image
import logging,os,time,base64
import numpy as np
import cv2 as cv

global query,datasets,cosineColor,cosineTexture
query = []
datasets = []

vectorInputC = []
vectorInputT= []
cosineColor = []
cosineTexture = []


app = Flask(__name__)
CORS(app)
app.logger.setLevel(logging.DEBUG)

def fileToBase64(file):
    img = Image.open(file)
    buffered = BytesIO()
    img.save(buffered, format="PNG" )
    base64Img = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return base64Img

def base64toBGR(string):
    imgByte = base64.b64decode(string)
    npImg = np.frombuffer(imgByte, np.uint8)
    bgr = cv.imdecode(npImg, cv.IMREAD_COLOR)
    return bgr

def bgrToBase64(matrix):
    bgr_image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
    _, buffer = cv.imencode('.png', bgr_image)
    base64_image = base64.b64encode(buffer).decode('utf-8')
    return base64_image

def searchColor():
    list = []
    for data in datasets:
        dictionary = {}
        res = runColor(query[0],data)
        if res > 0.6:
            dictionary["path"] = bgrToBase64(data)
            dictionary["cosine"] = round(res * 100,2)
            list.append(dictionary)
    return sorted(list,key=lambda x: x['cosine'], reverse=True)

def searchTexture():
    list = []
    for data in datasets:
        dictionary = {}
        res = runColor(query[0],data)
        if res > 0.6:
            dictionary["path"] = bgrToBase64(data)
            dictionary["cosine"] = round(res * 100,2)
            list.append(dictionary)
    return sorted(list,key=lambda x: x['cosine'], reverse=True)

def getVectorColor(matrix):
    img = normBGRtoHSV(matrix)
    return get3X3Histograms(img)

def testColor():
    list = []
    for i in range(len(datasets)):
        dictionary = {}
        res = getSimilarityIndeks(vectorInputC[0], cosineColor[i])
        if (res > 0.6):
            dictionary["path"] = datasets[i]
            dictionary["cosine"] = round(res * 100,2)
            list.append(dictionary)
    return sorted(list,key=lambda x: x['cosine'], reverse=True)

def testTexture():
    list = []
    for i in range(len(datasets)):
        dictionary = {}
        res = getSimilarityIndeks(vectorInputT[0], cosineTexture[i])
        if (res > 0.6):
            dictionary["path"] = datasets[i]
            dictionary["cosine"] = round(res * 100,2)
            list.append(dictionary)
    return sorted(list,key=lambda x: x['cosine'], reverse=True)



# Post an image to Upload folder and a folder of images to Dataset folder
@app.route('/api/upload', methods=['POST'])
def upload():
    app.logger.debug('Received a request to /api/upload')
    try:
        global query, datasets,cosineTexture,cosineColor
        cosineColor = []
        cosineTexture = []
        if 'image' in request.files:
            query = []
            app.logger.debug('Image found in request')
            image = request.files['image']
            query.append(base64toBGR(fileToBase64(image)))
            color = getVectorColor(query[0])
            vectorInputC.append(color)
            texture = getVectorTexture(query[0])
            vectorInputT.append(texture)
            return jsonify({"message": "File uploaded successfully"})
        elif 'dataset' in request.files:
            datasets = []
            dataset_files = request.files.getlist('dataset')
            app.logger.debug(f"Received dataset files: {dataset_files}")
            for dataset in dataset_files:
                mat = base64toBGR(fileToBase64(dataset))
                datasets.append(mat)
                color = getVectorColor(mat)
                cosineColor.append(color)
                texture = getVectorTexture(mat)
                cosineTexture.append(texture)
                return jsonify({"message": "Dataset uploaded successfully"})
        return jsonify({"error": "No file provided"}, 400)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

# def upload():
#     app.logger.debug('Received a request to /api/upload')
#     try:
#         if not os.path.isdir(base_path):
#             os.mkdir(base_path)

#         if 'image' in request.files:
#             app.logger.debug('Image found in request')
#             if not os.path.isdir(UPLOAD_IMAGE):
#                 os.mkdir(UPLOAD_IMAGE)
#             image = request.files['image']
#             filename = secure_filename(image.filename)
#             path = os.path.join(UPLOAD_IMAGE, filename)
#             files = os.listdir(UPLOAD_IMAGE)
#             if files:
#                 for file in files:
#                     os.remove(os.path.join(UPLOAD_IMAGE, file))
#             image.save(path)
#             return jsonify({"message": "File uploaded successfully"})
#         elif 'dataset' in request.files:
#             app.logger.debug('Dataset found in request')
#             if not os.path.isdir(UPLOAD_DATASET):
#                 os.mkdir(UPLOAD_DATASET)
#             dataset_files = request.files.getlist('dataset')
#             app.logger.debug(f"Received dataset files: {dataset_files}")
#             files = os.listdir(UPLOAD_DATASET)
#             if files:
#                 for file in files:
#                     os.remove(os.path.join(UPLOAD_DATASET, file))
#             for dataset in dataset_files:
#                 dataset_name = secure_filename(dataset.filename)
#                 dataset_path = os.path.join(UPLOAD_DATASET, dataset_name)
#                 dataset.save(dataset_path)
#             return jsonify({"message": "Dataset uploaded successfully"})
#         return jsonify({"error": "No file provided"}, 400)
#     except Exception as e:
#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Endpoint for using the CBIR functions
@app.route('/api/cbir', methods=['POST','GET'])
def run():
    app.logger.debug('Received a request to /api/cbir')
    # Return the run time (start time - end time)
    try:
        if request.method == 'POST':
            option = request.json.get('option')
            if option == 'color':
                app.logger.debug('Color method found in request')
                start_time = time.time()
                result = testColor()
            elif option == 'texture':
                app.logger.debug('Texture method found in request')
                start_time = time.time()
                result = testTexture()
            else:
                return jsonify({"error": "Invalid option"}), 400

            end_time = time.time()
            delta_time = end_time - start_time
            return jsonify({"result": result, "delta_time": delta_time})

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

    pass

if __name__ == '__main__':
    app.run(debug=True)

