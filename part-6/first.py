from tokenize import Ignore
from django.test import ignore_warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException,ElementNotSelectableException
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window()
# implicitly_wait
# driver.implicitly_wait(10) #Seconds
# explicit_wait declaration
mywait = WebDriverWait(driver,10,poll_frequency=2, ignored_exceptions = [
                       NoSuchElementException,
                       ElementNotVisibleException,
                       ElementNotSelectableException,
                       Exception
                       ])
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys('Selenium') # pass the value or search  the value
search_box.submit() # press enter keyword

#Explicitly
searchlink = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
searchlink.click() 
# driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()