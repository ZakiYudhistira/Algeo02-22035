from flask import Flask, render_template,request,jsonify,send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from ImageProcessingLibrary import *
import logging,os  
import time

app = Flask(__name__)
CORS(app)
app.logger.setLevel(logging.DEBUG)


relPaths = {}
imagepath =""
absPath = []

#  Path Image, Dataset, and Download Folder
base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"src","my-app","public")
UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")

def searchColor():
    dictionary = {}
    i = 0
    for filename in os.listdir(UPLOAD_DATASET):
        path_current = os.path.join("..", "public", "Dataset", filename)
        res = runColor(imagepath,absPath[i])
        i += 1
        if res > 0.6:
            dictionary[path_current] = res
    return dictionary

def searchTexture():
    dictionary = {}
    i = 0
    for filename in os.listdir(UPLOAD_DATASET):
        path_current = os.path.join("..", "public", "Dataset", filename)
        res = runTexture(imagepath,absPath[i])
        i += 1
        if res > 0.6:
            dictionary[path_current] = res
    return dictionary

# def searchColor():
#     global absPath,imagepath
#     i=0
#     for key in relPaths.keys():
#         res = runColor(imagepath,absPath[i])
#         i += 1
#         if res > 0.6:
#             relPaths[key] = round(res*100,2)
#         return relPaths


# def searchTexture():
#     global absPath,relPaths,imagepath
#     i=0
#     for key in relPaths.keys():
#         res = runTexture(imagepath,absPath[i])
#         i += 1
#         if res > 0.6:
#             relPaths[key] = round(res*100,2)
#     return dict(sorted(relPaths.items(), key=lambda item: item[1], reverse=True))

# Post an image to Upload folder and a folder of images to Dataset folder
@app.route('/api/upload', methods=['POST'])
def upload():
    global imagepath, relPaths, absPath
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

            return jsonify({"message": "File uploaded successfully"})
        elif 'dataset' in request.files:
            relPaths = {}
            absPath = []

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
                absPath.append(dataset_path)
                dataset.save(dataset_path)
            return jsonify({"message": "Dataset uploaded successfully"})
        return jsonify({"error": "No file provided"}, 400)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
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
                result = searchColor()
            elif option == 'texture':
                app.logger.debug('Texture method found in request')
                start_time = time.time()
                result = searchTexture()
            else:
                return jsonify({"error": "Invalid option"}), 400

            end_time = time.time()
            delta_time = end_time - start_time
            sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
            return jsonify({"result": sorted_result, "delta_time": delta_time})

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