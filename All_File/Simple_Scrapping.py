import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service("D:\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.NAME, "q").send_keys("list of watch name")
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
# name_one_watch_name = driver.find_element(By.CLASS_NAME,  "TrT0Xe")
name = driver.find_element(By.CLASS_NAME, "RqBzHd")
print(name.text)
heading_= driver.find_element(By.PARTIAL_LINK_TEXT,"The World's Best Luxury Watch Brands - Luxe ").click()
names_ = driver.find_element(By.CLASS_NAME, "entry-meta")

print(names_.text)
# print(name_one_watch_name.text)
time.sleep(15)
print(driver.title)
print(driver.current_url)
driver.close()
