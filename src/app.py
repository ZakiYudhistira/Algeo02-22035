
from flask import Flask, render_template
import os
 
app = Flask(__name__)

base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"test")

UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")

@app.route('/')
def cbir():
    return render_template('image_render.html')
 
if __name__ == '__main__':
    app.run(debug=True, port=8080)