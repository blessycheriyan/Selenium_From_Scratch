from operator import le
from re import L
import time
from tabnanny import check
from tokenize import Ignore
from django.test import ignore_warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException,ElementNotSelectableException
driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
# Click on link
driver.find_element(By.LINK_TEXT, "Digital downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Digital down").click()

# # Total number  of link
# links = driver.find_elements(By.TAG_NAME, "a")
links = driver.find_elements(By.XPATH, "//a")
print("Total number of links",len(links))

# print all links name
for link in links:
    print(link.text)