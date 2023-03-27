from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("D:\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# driver.find_element(By.ID, "small-searchterms").send_keys('Lenovo Thinkpad X1 Carbon Laptop')

driver.find_element(By.NAME, "q").send_keys('Lenovo Thinkpad X1 Carbon Laptop')
# driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Regist").click()