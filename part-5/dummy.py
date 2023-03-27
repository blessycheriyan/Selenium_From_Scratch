from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/register')
driver.get('https://www.snapdeal.com/')
driver.maximize_window()
#   Navigational Commands--------------------
time.sleep(3)
driver.back() # back to nopcommerce site
driver.forward() # forward to snapdeal site
driver.refresh() # refresh site 