
from flask import Flask, render_template,jsonif
from flask_cors import CORS
import os
 
app = Flask(__name__)
CORS(app)

base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"test")

UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")

@app.route('/api/upload', methods=['POST'])
def upload():
    if not os.path.isdir(base_path):
        os.mkdir(base_path)
    if not os.path
    
    

 
if __name__ == '__main__':
    app.run(debug=True)