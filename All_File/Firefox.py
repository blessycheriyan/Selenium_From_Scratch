from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("D:\geckodriver.exe")
driver = webdriver.Firefox(service=s)
# driver.maximize_window()
# driver.get('https://www.mozilla.org/en-US/firefox/')
# myPageTitle = driver.title
# print(myPageTitle)
# assert  "Google" in myPageTitle
# driver.quit()
# print(driver.quit())
