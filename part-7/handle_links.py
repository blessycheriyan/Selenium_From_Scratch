from operator import le
from re import L
import time
from tabnanny import check
from tokenize import Ignore
from django.test import ignore_warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
driver = webdriver.Chrome()
driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()

# Total number  of link
all_links = driver.find_elements(By.TAG_NAME, "a")
count =0
for link in all_links:
    url = link.get_attribute("href")
    try:
        response = requests.head(url)
    except:
        None    
    if response.status_code >= 400:
        print(url,"is broken")
        count +=1
    else:
        print(url,"is valid")    
print("Total number of count:",count)    
     

