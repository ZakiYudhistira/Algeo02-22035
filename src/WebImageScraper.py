import requests
from bs4 import BeautifulSoup
from PIL import Image
import os
import io
import time

# Function to create the folder if it doesn't exist
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def getRawHTML(url: str):
    data = requests.get(url, verify=True)
    return data.text

def scrapeImage(url: str, save_folder: str):
    # Create the folder if it doesn't exist
    create_folder_if_not_exists(save_folder)

    html = getRawHTML(url)
    html_parsed = BeautifulSoup(html, 'html.parser')
    image_urls = []

    for img_tag in html_parsed.find_all('img'):
        src = img_tag.get('src')
        if src:
            image_urls.append(src)

    count = 1
    for url in image_urls:
        try:
            image_content = requests.get(url).content
            if image_content:
                image_file = io.BytesIO(image_content)
                image = Image.open(image_file).convert("RGBA")

                # Save the image to the specified folder
                image_path = os.path.join(save_folder, f"{count}__{time.time()}_image.png")
                image.save(image_path, format="PNG", quality=80)

                count += 1
        except Exception as e:
            print(f"Error saving image: {e}")