
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
# find_element() - Returns the single webelement
# Locator matching with single element

# driver.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys('Apple MacBook Pro 13-inch')

# Locator matching with single element

# element = driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)

# Element nit available then throw NoSuchElementException

# element = driver.find_element(By.LINK_TEXT,"Log").click()

# find_element()s - Returns the Multiple webelement
# Locator matching with Multiple element

#element= driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# element[0].send_keys('Apple MacBook Pro 13-inch')

# Locator matching with multiple element

# elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")

# for ele in elements:
#     print(ele.text)

# Element nit available - Zero

element = driver.find_elements(By.LINK_TEXT,"Log")
print(len(element))
    
