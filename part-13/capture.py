from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
location = os.getcwd()
driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# driver.save_screenshot("D:\\Selenium\\part-13\\homepage.png")
driver.save_screenshot(os.getcwd() +"\\homepage.png")
driver.get_screenshot_as_file(os.getcwd() +"\\homepage.png")

# save it as binary format
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64()