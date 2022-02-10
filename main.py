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

chrome_options=Options()
chrome_options.add_argument("--user-data-dir2=chrome-data")
driver = webdriver.Chrome('chromedriver',options=chrome_options)
driver.get('https://bepro.digital')