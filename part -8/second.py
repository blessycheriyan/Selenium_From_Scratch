from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://mypage.rediff.com/login/dologin')
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(5)

alert_window = driver.switch_to.alert
print(alert_window.text)

alert_window.send_keys('Welcome')
alert_window.accept() # close alert window by ok button
