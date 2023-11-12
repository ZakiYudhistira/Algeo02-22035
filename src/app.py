from flask import Flask, render_template,jsonify
import os
app = Flask(__name__)

# app.middleware = [
#     'flask_cors.CORS',
#     {'AllowedOriginsMiddleware': ('*',)},
# ]

base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"test")

UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask API!'}
    return jsonify(data)

# @app.route('/api/cbir-color', methods=['POST'])
# def cbir_color():
#     return 'Hello, World!'
 
if __name__ == '__main__':
    app.run(debug=True)