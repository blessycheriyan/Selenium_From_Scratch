
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)
alert_window =driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys('Welcome')
alert_window.accept() # close alert window by ok button
# alert_window.dismiss() # close alert window by cancel button