from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("D:\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
assert "dashboard" in driver.current_url
driver.find_element(By.XPATH, "//input[@value='LOGIN']").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Welcome']").click()
time.sleep(3)