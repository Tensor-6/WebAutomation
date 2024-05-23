import ModLoad

depen = ['selenium']
ModLoad.importDependencies(depen)

import selenium
from selenium import webdriver
print(1)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = [
       "?widgetId=b4059e75-9755-401f-a7b5-d7c75361420d&redirectedFromEmbededMode=False&classId=c1a62643-ec0e-a373-347f-14d0a91315fb&occurrenceDate=20240524",

       ]

driver = webdriver.Firefox()
driver.get(url[0] )
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source