from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# Pop the disable pop 
driver = webdriver.Chrome()
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')

driver.maximize_window()

# # Scroll down by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels",value)

# # Scroll down page till the element is visible 

# flag= driver.find_element(By.XPATH,"//td[normalize-space()='India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels",value)

# Scroll down page till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels",value)

time.sleep(5)
# Scroll up to starting page

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels",value)