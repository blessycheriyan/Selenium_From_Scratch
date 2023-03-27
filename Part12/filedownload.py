from click import option
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    # download desired location
    preferences = {
        'download.default_directory': location ,
        "plugins.always_open_pdf_externally":True
    }
    ops =webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options = ops)
    return driver

driver = chrome_setup()
driver.get('https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/')
driver.maximize_window()

input1 =  driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
