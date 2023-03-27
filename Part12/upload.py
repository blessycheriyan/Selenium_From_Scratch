from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# import KEYS
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.foundit.in/')

driver.maximize_window()

driver.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn secondaryBtn']").click()
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys('D:\Selenium\sample.pdf')
