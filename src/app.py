
from flask import Flask, render_template,request,jsonify,send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
    
import os
app = Flask(__name__)
CORS(app)

# app.middleware = [
#     'flask_cors.CORS',
#     {'AllowedOriginsMiddleware': ('*',)},
# ]

base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"test")

UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")

@app.route('/api/upload', methods=['POST'])
def upload():
    try :
        if not os.path.isdir(base_path):
            os.mkdir(base_path)
        if 'image' in request.files:
            if not os.path.isdir(UPLOAD_IMAGE):
                os.mkdir(UPLOAD_IMAGE)
            image = request.files['image']
            filename = secure_filename(image.filename)
            path = os.path.join(UPLOAD_IMAGE,filename)
            if os.path.isfile(path):
                os.remove(path)
            files = os.listdir(UPLOAD_IMAGE)
            if (files):
                for file in files:
                    os.remove(os.path.join(UPLOAD_IMAGE,file))
            image.save(path)
            return jsonify ({"message": "File uploaded successfully"})
        return jsonify(({"error": "No file provided"}), 400)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
        

 
if __name__ == '__main__':
    app.run(debug=True)