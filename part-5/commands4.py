
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://admin-demo.nopcommerce.com/')
driver.maximize_window()
# find_element() - Returns the single webelement

elements = driver.find_element(By.XPATH, "//input[@id='Email']")
elements.clear()

elements.send_keys('james@example')
# text - returns the inner text of the element
print(elements.text)
# get_attributes - returns the value of any web element
print(elements.get_attribute('value'))
