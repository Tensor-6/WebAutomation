#simple moudle downloader
#add cross-platofrm capability
import ModLoad
depen = ['selenium',
       'cryptography',
       'webdriver-manager',
       'schedule',
       'mouse'
       ]
#ModLoad.importDependencies(depen)

import os
import json
import time
import base64
import easyocr
import OCRclick
import schedule
import datetime
import selenium
import pyautogui
import random as r
from PIL import ImageGrab
import undetected_chromedriver as uc
from cryptography.fernet import Fernet
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#custom module imports
import ParisCrypts as crypt
import Scheduler as sched

url = [
       "https://cityofsurrey.perfectmind.com/23615/Clients/BookMe4LandingPages/Class?widgetId=b4059e75-9755-401f-a7b5-d7c75361420d&redirectedFromEmbededMode=False&classId=e50e6837-9141-4ffe-a5fa-4c80c86c8cc3&occurrenceDate=20240605",
       "https://cityofsurrey.perfectmind.com/23615/Clients/BookMe4LandingPages/Class?widgetId=b4059e75-9755-401f-a7b5-d7c75361420d&redirectedFromEmbededMode=False&classId=c11f380a-9567-402d-b1c2-f4c7ead23863&occurrenceDate=20240605",
       'https://cityofsurrey.perfectmind.com/23615/Clients/BookMe4LandingPages/Class?widgetId=b4059e75-9755-401f-a7b5-d7c75361420d&redirectedFromEmbededMode=False&classId=1e1495fe-a10c-42e8-aa51-808680e293c2&occurrenceDate=20240604'
       ]
debug = False
emuPsn = True

def move_text_on_screen(text, delay=1):
    def find_text_coordinates(image_path, text):
        # Create an EasyOCR reader
        reader = easyocr.Reader(['en'])

        # Perform OCR on the image
        results = reader.readtext(image_path)

        # Loop through the OCR results and find the coordinates of the specified text
        for (bbox, word, confidence) in results:
            if word.lower() == text.lower():
                # bbox contains the coordinates of the bounding box
                (top_left, top_right, bottom_right, bottom_left) = bbox
                return (top_left, top_right, bottom_right, bottom_left)

        return None

    # Capture the screen and save it to a file
    screenshot = pyautogui.screenshot()
    screenshot_path = 'TempScreenshot.png'
    screenshot.save(screenshot_path)

    # Find the coordinates of the string 'Next' on the screenshot
    coordinates = find_text_coordinates(screenshot_path, text)

    if coordinates:
        # Calculate the center of the bounding box
        (top_left, top_right, bottom_right, bottom_left) = coordinates
        center_x = int((top_left[0] + bottom_right[0]) / 2)
        center_y = int((top_left[1] + bottom_right[1]) / 2)

        # Move the mouse to the center of the bounding box and click
        pyautogui.moveTo(center_x, center_y, duration=delay)

        print(f"'{text}': {center_x}, {center_y}")
    else:
        print(f"'{text}' not found on the screen")

def EmuWait():
    if emuPsn:
        time.sleep(r.uniform(0.5, 2.0))
    else:
        pass

class BadmintonRegBot:
    def __init__(self, password):
        try:
            saltf = open('salt.txt', 'r')
            if debug:
                print('sucess open salt')
            salt = base64.urlsafe_b64decode(saltf.read().encode('utf-8'))
            if debug:
                print(salt)
        except:
            salt = None
        self.encry = crypt.StringEncryptor(password, input('Regen Salt(true/false): ').lower(), salt)
        preset = 'EncryPrst.json'
        #write create file
        overwrite = input("Overwrite preset(true/false): ")
        if overwrite.lower() == 'true':
            data = {
                'MySEmail':self.encry.encrypt(str(input('Enter MySurrey email: '))),
                'password':self.encry.encrypt(str(input('Enter MySurrey password: '))),
                'cardName':self.encry.encrypt(str(input('Enter your credit card name: '))),
                'cardNumb':self.encry.encrypt(str(input('Enter your credit card number: '))),
                'cardExpM':self.encry.encrypt(str(input('Enter the expiry month(1-12): '))),
                'cardExpY':self.encry.encrypt(str(input('Enter card expiry year(2XXX): '))),
                'cardCvvB':self.encry.encrypt(str(input('Card Cvv (XXX): '))),
                'regiMemb':self.encry.encrypt(str(input('Enter member: '))),
                'billadrs':self.encry.encrypt(str(input('Enter your billing adress: '))),
                'billcity':self.encry.encrypt(str(input('Enter your billing city: '))),
                'billcout':self.encry.encrypt(str(input('Enter the country: '))),
                'billprov':self.encry.encrypt(str(input('Enter the province: '))),
                'pstlcode':self.encry.encrypt(str(input('Postal Code: ')))
            }
            with open(preset, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"File created and data saved: {preset}")

        #open read file
        with open(preset, 'r') as json_file:
            data = json.load(json_file)
        self.MySEmail = data['MySEmail']
        self.password = data['password']
        self.cardname = data['cardName']
        self.cardnumb = data['cardNumb']
        self.cardmont = data['cardExpM']
        self.cardyear = data['cardExpY']
        self.cardcvvb = data['cardCvvB']
        self.regiMemb = data['regiMemb']
        self.billAdrs = data['billadrs']
        self.billCity = data['billcity']
        self.billCout = data['billcout']
        self.billProv = data['billprov']
        self.pstlCode = data['pstlcode']

    def navigate(self):
        driver = uc.Chrome()
        driver.maximize_window()
        driver.get(url[0]) #add date funct
        #time.sleep(10)
        regiTag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bm-button.bm-book-button')))
        #regiTag = driver.find_element(By.CSS_SELECTOR, '.bm-button.bm-book-button')
        regiTag.click()
        EmuWait()
        LogInEmlIn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'emailid')))
        LogInEmlIn.send_keys(self.encry.decrypt(self.MySEmail))
        EmuWait()
        LogInPslIn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'loginradius-login-password')))
        LogInPslIn.send_keys(self.encry.decrypt(self.password))
        EmuWait()
        SignInBtn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'loginradius-validate-login')))
        SignInBtn.click()
        EmuWait()
        wait = WebDriverWait(driver, 20)
        try:
            memberBtn = driver.find_element(By.ID, wait.until(EC.presence_of_element_located((By.XPATH, f"//label[text()='{self.encry.decrypt(self.regiMemb)}']"))).get_attribute("for"))
        except:
            memberBtn = driver.find_element(By.ID, wait.until(EC.presence_of_element_located((By.XPATH, f"//label[text()='{self.encry.decrypt(self.regiMemb) + ' (You)'}']"))).get_attribute("for"))
        memberBtn.click()
        EmuWait()
        contBtn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Next']"))) 
        contBtn.click()
        '''nextBtn = WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Add to Cart' and @class='bm-button']")))
        position = nextBtn.location
        x = position['x']
        y = position['y']
        print(f'Element position: x={x}, y={y}')
        size = nextBtn.size
        width = size['width']
        height = size['height']
        print(f'Element size: width={width}, height={height}')
        x = position['x'] + size['width'] / 2
        y = position['y'] + size['height'] / 2
        time.sleep(1)
        pyautogui.moveTo(x, y+70)
        pyautogui.click()'''
        #click_text_on_screen('next')
        OCRclick.move_text_on_screen('next')
        pyautogui.click()

        EmuWait()
        #checkout
        driver.switch_to.frame(WebDriverWait(driver, 2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.online-store'))))
        cardNameF = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-bind*="floatingLabel: creditCard.nameOnCard"][class*="floating-label transform empty"]')))
        cardNameF.send_keys(self.encry.decrypt(self.cardname))
        EmuWait()
        cardNumbF = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-bind*="floatingLabel: creditCard.cardNumber"][class*="floating-label transform empty"]')))
        cardNumbF.send_keys(self.encry.decrypt(self.cardnumb))
        EmuWait()
        select = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'section'))).find_elements(By.TAG_NAME, 'select')[0])
        select.select_by_value(self.encry.decrypt(self.cardmont))
        select = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'section'))).find_elements(By.TAG_NAME, 'select')[1])
        select.select_by_value(self.encry.decrypt(self.cardyear))
        EmuWait()
        '''OCRclick.move_text_on_screen('CVV')
        pyautogui.moveRel(None, 30)
        pyautogui.click()
        pyautogui.write(self.encry.decrypt(self.cardcvvb))
        '''
        cardCVV = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        print('cvv selected')
        cardCVV.send_keys(self.encry.decrypt(self.cardcvvb))
        print('cvv success')
        '''except:
            print(6)
            pass'''#ADREWSS
        EmuWait()
        ADREWSS = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"][data-bind*="floatingLabel: creditCard.billingAddress.street"][class*="floating-label transform empty"]')))
        ADREWSS.send_keys(self.encry.decrypt(self.billAdrs))
        EmuWait()
        ADREWSS = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"][data-bind*="floatingLabel: creditCard.billingAddress.city"][class*="floating-label transform empty"]')))
        ADREWSS.send_keys(self.encry.decrypt(self.billCity))
        EmuWait()
        select = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'section'))).find_elements(By.TAG_NAME, 'select')[0])
        select.select_by_value(self.encry.decrypt(self.cardmont))
        select = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'section'))).find_elements(By.TAG_NAME, 'select')[1])
        select.select_by_value(self.encry.decrypt(self.cardyear))
        EmuWait()
        '''OCRclick.move_text_on_screen('CVV')
        pyautogui.moveRel(None, 30)
        pyautogui.click()
        pyautogui.write(self.encry.decrypt(self.cardcvvb))
        '''
        cardCVV = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        print('cvv selected')
        cardCVV.send_keys(self.encry.decrypt(self.cardcvvb))
        print('cvv success')
        time.sleep(6000)
        driver.quit()
    
    def simClickID(self, tag):
        time.sleep(2)
        nextBtn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, tag)))
        position = nextBtn.location
        x = position['x']
        y = position['y']
        print(f'Element position: x={x}, y={y}')
        size = nextBtn.size
        width = size['width']
        height = size['height']
        print(f'Element size: width={width}, height={height}')
        x = position['x'] + size['width'] / 2
        y = position['y'] + size['height'] / 2
        time.sleep(1)
        pyautogui.moveTo(x, y+70)
        pyautogui.click()

class OverArch:
    def __init__(self):
        #self.password = input('password: ')
        self.BadRB =BadmintonRegBot(self.password)
    def FridayBadmintonLoop(self):
        #loope weekly tues 7:15pm
        self.sch = sched.Scheduler()
        self.sch.schedule_task('sunday', '14:24', 3, 'seconds', self.BadRB.navigate)

'''
r = OverArch()
r.FridayBadmintonLoop()
'''
b = BadmintonRegBot(input('password: '))
b.navigate()
