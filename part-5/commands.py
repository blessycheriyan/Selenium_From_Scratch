from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
# title & current_url
print(driver.title)
print(driver.current_url)
print(driver.page_source)
