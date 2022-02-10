###
import pandas as pd
import re

#Para llamar al chromedriver
from selenium import webdriver

#Espera un tiempo hasta que cargue el elemento ui en el DOM
from selenium.webdriver.support.ui import WebDriverWait

#Activa las capacidades para interactuar con el chromedriver
from selenium.webdriver.chrome.options import Options

#Enviar informacion a la ui
from selenium.webdriver.common.keys import Keys
import os
import time

print('Abriendo sitio web')

#chrome_options=Options()
#driver = webdriver.Chrome('chromedriver',options=chrome_options)

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--user-data-dir2=chrome-data")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
browser.get('https://bepro.digital')