from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
# window_id =driver.current_window_handle
# print(window_id)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
window_ID = driver.window_handles
parentwindowid = window_ID[0]
childwindowid = window_ID[1]

# print(parentwindowid)
driver.switch_to_window(childwindowid)
print(driver.title)
driver.switch_to_window(parentwindowid)
print(driver.title)

# Approch2 

for winid in window_ID:
    driver.switch_to_window(winid)
    if driver.title == "Orange":
        driver.close