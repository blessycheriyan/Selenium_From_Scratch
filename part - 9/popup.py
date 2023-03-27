
from optparse import Option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Pop the disable pop 
ops = webdriver.ChromeOptions()
ops.add_argument('--disable notification')
driver = webdriver.Chrome(options = ops)
driver.get('https://whatmylocation.com/')

driver.maximize_window()
