from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Apply for vendor account").click()
time.sleep(3)
# driver.close()
# driver.quit()

