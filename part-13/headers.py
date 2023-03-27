from click import option
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()
def headless_chromes():
    from selenium.webdriver.chrome.service import Service
   
    ops =webdriver.ChromeOptions()
    ops.headless= True
    # no open page for chrome
    driver = webdriver.Chrome(options = ops)
    return driver

driver = headless_chromes()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

print(driver.title)