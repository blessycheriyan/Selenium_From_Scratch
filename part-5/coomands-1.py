
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()

display_= driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print(display_.is_displayed())
print(display_.is_enabled()) # pass through values

Male_radio_btn= driver.find_element(By.XPATH, "//input[@id='gender-male']")
Male_radio_btn.click() 
print(Male_radio_btn.is_selected()) # clicking through radio btn
