
from flask import Flask, render_template,request,jsonify,send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import logging,os

import sys
sys.path.append(os.path.join(os.path.dirname(__file__),"..","..","ImageProcessingLibrary"))
from ImageProcessingLibrary import *

app = Flask(__name__)
CORS(app)

# app.middleware = [
#     'flask_cors.CORS',
#     {'AllowedOriginsMiddleware': ('*',)},
# ]

base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"test")
app.logger.setLevel(logging.DEBUG)

UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")

# Post an image to Upload folder and a folder of images to Dataset folder
@app.route('/api/upload', methods=['POST'])
def upload():
    app.logger.debug('Received a request to /api/upload')
    try:
        if not os.path.isdir(base_path):
            os.mkdir(base_path)

        if 'image' in request.files:
            app.logger.debug('Image found in request')
            if not os.path.isdir(UPLOAD_IMAGE):
                os.mkdir(UPLOAD_IMAGE)
            image = request.files['image']
            filename = secure_filename(image.filename)
            path = os.path.join(UPLOAD_IMAGE, filename)
            files = os.listdir(UPLOAD_IMAGE)
            if files:
                for file in files:
                    os.remove(os.path.join(UPLOAD_IMAGE, file))
            image.save(path)
            return jsonify({"message": "File uploaded successfully"})
        elif 'dataset' in request.files:
            app.logger.debug('Dataset found in request')
            if not os.path.isdir(UPLOAD_DATASET):
                os.mkdir(UPLOAD_DATASET)
            dataset_files = request.files.getlist('dataset')
            app.logger.debug(f"Received dataset files: {dataset_files}")
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

# Call all functions of calculations (Warna)
@app.route('/api/cosine', methods=['GET'])
def runColor():
    app.logger.debug("Received a request to /api/cosine")
    image1 = cv.imread("D:/Main Files/File Amel/Program/Tubes Algeo 2/Algeo02-22035/test/Upload/download_5.jpeg")
    image2 = cv.imread("D:/Main Files/File Amel/Program/Tubes Algeo 2/Algeo02-22035/test/Images/apple.jpg")

    img1 = normBGRtoHSV(image1)
    img2 = normBGRtoHSV(image2)

    value = round(getSimilarityIndeks(get3X3Histograms(img1),get3X3Histograms(img2)) * 100, 2)

    return(str(value))


# Call all functions of calculations (Tekstur)
 
if __name__ == '__main__':
    app.run(debug=True)