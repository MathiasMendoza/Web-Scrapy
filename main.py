import time
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import requests
from PIL import Image
import io


# BING URL AND QUERY
bing = 'https://bing.com/images/search?q='
query = input("Search for: ")
url = bing + query

# CHROME DRIVER
driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
driver.get(url)

# CHECK FOR DIR AND CREATE IT IF NOT
dir = 'C:\\Users\\Useer\\Desktop\\Images\\' + query
if not os.path.isdir(dir):
    os.mkdir(dir)

# SCROLLING TO THE END OF THE PAGE
i = 0
while i <= 4:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    i += 1
    time.sleep(10)

# FIND IMAGES AND LOOPING THROUGH THEM
images = driver.find_elements_by_tag_name('img')
nro = 1
for img in images:
    try:
        src = img.get_attribute('src')
        image_content = requests.get(src).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = dir + '\\Image' + str(nro) + '.jpg'
        with open(file_path, 'wb') as f:
            image.save(f, 'JPEG', quality= 85)
        print("Success - saved {} on {}".format(src, file_path))
        nro+=1

    except Exception as e:
        print("Error - could not save image from url {} - {}".format(url, e))

