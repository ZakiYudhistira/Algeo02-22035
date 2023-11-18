import requests
from bs4 import BeautifulSoup
from PIL import Image
import io

def getRawHTML(url : str):
    data = requests.get(url, verify=True)
    return data.text

def scrapeImage(url : str):
    html = getRawHTML(url)
    html_parsed = BeautifulSoup(html, 'html.parser')
    image_url = []
    for i in html_parsed.findAll('img'):
        image_url.append(i['src'])
    count = 1
    for url in image_url:
        print(url)
        try:
            image_content = requests.get(url).content

            image_file = io.BytesIO(image_content)

            image = Image.open(image_file).convert("RGBA")

            image.save(f"{count}_image.png", format="PNG", quality=80)
            count = count + 1
        except:
            pass


scrapeImage("https://www.google.com/search?q=kpop+faces&sca_esv=583597295&rlz=1C1CHZN_enID1043ID1043&tbm=isch&sxsrf=AM9HkKkdLNeLJd_k0vRy3Cl3kc44yG5M1Q:1700305910533&source=lnms&sa=X&sqi=2&ved=2ahUKEwju7bmOtc2CAxWHyzgGHUvWAtoQ_AUoAXoECAMQAw&biw=1646&bih=904&dpr=1.75")
# image_url = []
# for i in parsed.findAll('img'):
#      image_url.append(i['src'])

# count = 0
# for url in image_url:
#     print(url)
#     try:
#         image_content = requests.get("https:"+url).content

#         image_file = io.BytesIO(image_content)

#         image = Image.open(image_file).convert("RGBA")

#         image.save(f"{count}bom.png", format="PNG", quality=80)
#         count = count + 1
#     except:
#         pass
scrapeImage("https://en.wikipedia.org/wiki/Flag")
