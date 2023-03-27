from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.google.com/')
myPageTitle = driver.title
print(myPageTitle)

assert  "Google" in myPageTitle
# Searching for Python docs and press enter to search

driver.find_element(By.NAME, "q").send_keys('python docs',Keys.ENTER)
# driver.close()

############OUTPUT #################
# Google

