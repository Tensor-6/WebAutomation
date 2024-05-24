import ModLoad
import time
depen = ['selenium',
       'cryptography'
       ]
ModLoad.importDependencies(depen)

import base64
import selenium
from selenium import webdriver
from cryptography.fernet import Fernet
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

url = [
       "https://cityofsurrey.perfectmind.com/23615/Clients/BookMe4LandingPages/Class?widgetId=b4059e75-9755-401f-a7b5-d7c75361420d&redirectedFromEmbededMode=False&classId=c1a62643-ec0e-a373-347f-14d0a91315fb&occurrenceDate=20240524",
       "https://cityofsurrey.perfectmind.com/23615/Clients/BookMe4LandingPages/Class?widgetId=b4059e75-9755-401f-a7b5-d7c75361420d&redirectedFromEmbededMode=False&classId=32db5eaa-69d6-f210-e8ce-40a81856dff7&occurrenceDate=20240524"
       ]

driver = webdriver.Chrome()
driver.get(url[1] )
time.sleep(10)
#anchor = driver.find_element(By.CLASS_NAME, 'bm-button bm-book-button')
#anchor.click()
anchor_tag = driver.find_element(By.CSS_SELECTOR, '.bm-button.bm-book-button')
anchor_tag.click()
time.sleep(5)
LogInEmlIn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'emailid')))
LogInEmlIn.send_keys('testa@g.vb')
LogInPslIn = driver.find_element(By.ID, 'loginradius-login-password')
LogInPslIn.send_keys('testa@g.vb')
SignInBtn =  driver.find_element(By.ID, 'loginradius-validate-login')
time.sleep(6000)
driver.quit()