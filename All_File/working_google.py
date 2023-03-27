from _ast import Import
from datetime import time
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service("D:\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.NAME,"q").send_keys("LinkedIn login")
driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)
driver.find_element(By.PARTIAL_LINK_TEXT,"LinkedIn Login").click()
driver.find_element(By.ID,"username").send_keys('enter your username')
driver.find_element(By.ID,"password").send_keys('enter your password')
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)
print(driver.title)
print(driver.current_url)
driver.close()