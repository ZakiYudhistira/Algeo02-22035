from flask import Flask, render_template,request,jsonify,send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from ImageProcessingLibrary import *
import logging,os  
import time
 
app = Flask(__name__)
CORS(app)
app.logger.setLevel(logging.DEBUG)

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