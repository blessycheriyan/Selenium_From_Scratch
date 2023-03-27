from optparse import Option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# Pop the disable pop 
driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.find_element(By.NAME,"username").send_keys('Admin')
driver.find_element(By.NAME,"password").send_keys('admin123')
driver.find_element(By.TAG_NAME, "button").click()
# not working