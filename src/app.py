from flask import Flask, render_template,request,jsonify,send_from_directory, Response
from flask_cors import CORS
from werkzeug.utils import secure_filename
from ImageProcessingLibrary import *
import logging,os,time,multiprocessing

app = Flask(__name__)
CORS(app)
app.logger.setLevel(logging.DEBUG)

imagepath =""
imageVectorColor = None
imageVectorTexture = None

# Path Image, Dataset, and Download Folder
base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"src","my-app","public")
UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")

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

# 1. Endpoint to post an image to Upload folder and a folder of images to Dataset folder
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
    
# 2. Endpoint for using the CBIR functions
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
    
# 3. Endpoint for image scrapping
# @app.route('/api/scrap', methods=['POST'])

# 4. Endpoint for downloading the result as PDF
# @app.route('/api/download', methods=['POST'])
# def download():
#     app.logger.debug('Received a request to /api/download')
    
if __name__ == '__main__':
    app.run(debug=True)