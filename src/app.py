from flask import Flask,request,jsonify,send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from ImageProcessingLibrary import *
import logging,os,time,ast
import pandas as pd
import cv2 as cv
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor
from ImageProcessingLibrary import *
from WebImageScraper import *
from reportlab.pdfgen import canvas

app = Flask(__name__)
CORS(app)
app.logger.setLevel(logging.DEBUG)

imagepath =""
imageVectorColor = None
imageVectorTexture = None
download = []

# Path Image, Dataset, and Download Folder
base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"src","my-app","public")
UPLOAD_IMAGE = os.path.join(base_path,"Upload")
UPLOAD_DATASET = os.path.join(base_path,"Dataset")
DOWNLOAD_FOLDER = os.path.join(base_path,"Download")
CACHING_FOLDER= os.path.join(base_path,"Cache")

def writeCacheColor():
    vectors = []
    filenames = []
    if not os.path.exists(CACHING_FOLDER):
        os.makedirs(CACHING_FOLDER)

    for filename in os.listdir(UPLOAD_DATASET):
        img = cv.imread(os.path.join(UPLOAD_DATASET, filename))
        img = normBGRtoHSV(img)
        img = get3X3Histograms(img)
        vectors.append(img.tolist())  # Convert the numpy array to a Python list
        filenames.append(os.path.basename(filename))

    data = pd.DataFrame({"filename": filenames, "vectors": vectors})
    data.set_index("filename", inplace=True)  # Set 'filename' as the index
    data.to_csv(os.path.join(CACHING_FOLDER, "color_cache.csv"), header=False)


def getCache(csv_path):
    df = pd.read_csv(csv_path, header=None, names=['filename', 'vector'])
    df['vector'] = df['vector'].apply(ast.literal_eval)  
    data_dict = df.set_index('filename')['vector'].to_dict()
    return data_dict

def getVectorColor(path):
    img = cv.imread(path)
    img = normBGRtoHSV(img)
    return get3X3Histograms(img)

def searchColorCache():
    cacheColor = getCache(os.path.join(CACHING_FOLDER, "color_cache.csv"))
    data = []
    for key in cacheColor.keys():
        path_current = "/Dataset/" + key
        res = getSimilarityIndeks(imageVectorColor, cacheColor[key])
        if res is not None and res > 0.6:
            data.append({"path": path_current, "value": round(res * 100, 2)})
    sorted_data = sorted(data, key=lambda x: x["value"], reverse=True)
    return sorted_data

def processColor(args):
    base_vector, path = args
    res = getSimilarityIndeks(base_vector, getVectorColor(path))
    relPath = "/Dataset/" + os.path.basename(path)
    return {"path": relPath, "value": round(res * 100, 2)} if res > 0.6 else None


def colorParallel(base_vector, dataset_paths, parallel_processes):
    data = []
    args_list = [(base_vector, path) for path in dataset_paths]
    with ProcessPoolExecutor(max_workers=parallel_processes) as executor:
        results = list(executor.map(processColor, args_list))
    return [result for result in results if result]

def searchColorParallel(parallel_processes=60):
    global imageVectorColor
    
    if imageVectorColor is None:
        return jsonify({"error": "Base image vector not calculated"}), 400

    dataset_paths = [os.path.join(UPLOAD_DATASET, filename) for filename in os.listdir(UPLOAD_DATASET)]
    return sorted(colorParallel(imageVectorColor, dataset_paths, parallel_processes),key=lambda x:x["value"],reverse=True)

def processTexture(args):
    base_vector, path = args
    img1 = cv.imread(path)
    res = getSimilarityIndeks(base_vector, getVectorTexture(img1))
    relPath = "/Dataset/" + os.path.basename(path)
    return {"path": relPath, "value": round(res * 100, 2)} if res > 0.6 else None


def textureParallel(base_vector, dataset_paths, parallel_processes):
    args_list = [(base_vector, path) for path in dataset_paths]
    with ProcessPoolExecutor(max_workers=parallel_processes) as executor:
        results = list(executor.map(processTexture, args_list))
    return [result for result in results if result]

def searchColor():
    if os.path.exists(os.path.join(CACHING_FOLDER, "color_cache.csv")):
        print("Cache")
        return searchColorCache()
    else:
        print("Non-Cache")
        return searchColorParallel()

def searchTextureParallel(parallel_processes=60):
    global imageVectorTexture

    if imageVectorColor is None:
        return jsonify({"error": "Base image vector not calculated"}), 400

    dataset_paths = [os.path.join(UPLOAD_DATASET, filename) for filename in os.listdir(UPLOAD_DATASET)]
    return sorted(textureParallel(imageVectorTexture, dataset_paths, parallel_processes),key=lambda x:x["value"],reverse=True)

# Function to process the image in one go
def getVectorTexture(img):
    data = getCoOccurenceMatrix(getGrayScaleMatrix(img))
    data = getNormalizedSymmetryMatrix(getSymmetryMatrix(data))

    features = [extractFeature((data, func)) for func in [getContrast, getHomogeneity, getEntropy, getASM, getEnergy, getDissimilarity]]

    v = getVector(*features)
    return v

def extractFeature(args):
    data, func = args
    return func(data)

def writeCacheTexture():
    global cacheTexture
    vectors = []
    filenames = []

    for filename in os.listdir(UPLOAD_DATASET):
        img = cv.imread(os.path.join(UPLOAD_DATASET, filename))
        img = getVectorTexture(img)
        vectors.append(img.tolist())
        filenames.append(os.path.basename(filename))

    data = pd.DataFrame({"filename": filenames, "vectors": vectors})
    data.set_index("filename", inplace=True)  # Set 'filename' as the index
    data.to_csv(os.path.join(CACHING_FOLDER, "texture_cache.csv"), header=False)

    cacheTexture = getCache(os.path.join(CACHING_FOLDER, "texture_cache.csv"))

def searchTextureCache(): 
    cacheTexture = getCache(os.path.join(CACHING_FOLDER, "texture_cache.csv"))
    data = []
    for key in cacheTexture.keys():
        path_current = "/Dataset/" + key
        res = getSimilarityIndeks(imageVectorTexture, cacheTexture[key])
        if res is not None and res > 0.6:
            data.append({"path": path_current, "value": round(res * 100, 2)})
    sorted_data = sorted(data, key=lambda x: x["value"], reverse=True)
    return sorted_data

def searchTexture():
    if os.path.exists(os.path.join(CACHING_FOLDER, "texture_cache.csv")):
        print("Cache")
        return searchTextureCache()
    else:
        print("Non-Cache")
        return searchTextureParallel()


def writePDF(results):
    app.logger.debug('Writing PDF...')
    if not os.path.isdir(DOWNLOAD_FOLDER):
        os.mkdir(DOWNLOAD_FOLDER)
    pdf_path = os.path.join(DOWNLOAD_FOLDER, "results.pdf")

    pdf = canvas.Canvas(pdf_path)

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawCentredString(300, 770, "Reverse Image Search")
    pdf.drawCentredString(300, 750, "Keluarga Cemara")

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(30, 720, "Input Query Image")
    pathInput = os.listdir(UPLOAD_IMAGE)
    inputImg = os.path.join(UPLOAD_IMAGE, pathInput[0])
    pdf.drawInlineImage(inputImg, 30, 600, width=150, height=100)

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(30, 570, "Hasil Image Query")
    pdf.setFont("Helvetica", 12)
    y_position = 450

    for result in results:
        path = result.get('path', '')
        value = result.get('value', '')

        if y_position < 50:
            pdf.showPage()
            y_position = 700 

        image_path = os.path.join(UPLOAD_DATASET, os.path.basename(path))
        pdf.drawInlineImage(image_path, 30, y_position, width=150, height=100)
        text = f"Cosine Similarity: {value}%"
        pdf.drawString(210, y_position + 40, text)
        y_position -= 100

    pdf.save()

    app.logger.debug(f'PDF Path: {pdf_path}')
    return pdf_path


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
            img = cv.imread(path)
            imageVectorColor = getVectorColor(path)
            imageVectorTexture = getVectorTexture(img)
            print("VECTOR TEXTURE" ,imageVectorTexture)
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

            csvColor = os.path.join(CACHING_FOLDER, "color_cache.csv")
            if os.path.exists(csvColor):
                os.remove(csvColor)
            csvTexture = os.path.join(CACHING_FOLDER, "texture_cache.csv")
            if os.path.exists(csvTexture):
                os.remove(csvTexture)

            return jsonify({"message": "Dataset uploaded successfully"})
        return jsonify({"error": "No file provided"}, 400)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# 2. Endpoint for using the CBIR functions
@app.route('/api/cbir', methods=['POST', 'GET'])
def run():
    global cacheColor,download
    app.logger.debug('Received a request to /api/cbir')
    try:
        if request.method == 'POST':
            option = request.json.get('option')
            if not os.path.isdir(DOWNLOAD_FOLDER):
                os.mkdir(DOWNLOAD_FOLDER)
            down = os.listdir(DOWNLOAD_FOLDER)
            for file in down:
                os.remove(os.path.join(DOWNLOAD_FOLDER,file))
            if option == 'color':
                app.logger.debug('Color method found in request')
                start_time = time.time()
                result = searchColor()
                download = result
                if not os.path.exists(os.path.join(CACHING_FOLDER,"color_cache.csv")):
                    writeCacheColor()
            elif option == 'texture':
                app.logger.debug('Texture method found in request')
                start_time = time.time()
                result = searchTexture()
                download = result
                if not os.path.exists(os.path.join(CACHING_FOLDER,"texture_cache.csv")):
                    writeCacheTexture()
            else:
                return jsonify({"error": "Invalid option"}), 400

            end_time = time.time()
            delta_time = end_time - start_time
            # writePDF(result)
            return jsonify({"result": result, "delta_time" : delta_time})
        return jsonify({"error": "No method provided"}, 400)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
# 3. Endpoint for image scrapping
@app.route('/api/scrap', methods=['GET', 'POST'])
def scrapImages():
    try:
        app.logger.info("Received POST request to /api/scrap")
        url = request.json.get('url')
        if not url:
            return jsonify({"error": "No URL provided"}), 400
        else:
            if not os.path.exists(UPLOAD_DATASET):
                os.mkdir(UPLOAD_DATASET)
            if not os.path.exists(CACHING_FOLDER):
                os.mkdir(CACHING_FOLDER)

            files = os.listdir(UPLOAD_DATASET)
            if files:
                for file in files:
                    os.remove(os.path.join(UPLOAD_DATASET, file))
            files = os.listdir(CACHING_FOLDER)
            if files:
                for file in files:
                    os.remove(os.path.join(CACHING_FOLDER, file))

        scrapeImage(url, UPLOAD_DATASET)

        return jsonify({"message": "Image scraping successful"})
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# 4. Endpoint for downloading the result as PDF
@app.route('/api/download', methods=['POST'])
def downloadPDF():
    global download
    pdf_path = writePDF(download)
    return send_file(pdf_path, as_attachment=True, download_name='results.pdf')
    
if __name__ == '__main__':
    app.run(debug=True)