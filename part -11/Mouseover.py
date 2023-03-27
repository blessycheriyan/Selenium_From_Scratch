from optparse import Option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
# Pop the disable pop 
driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.find_element(By.NAME,"username").send_keys('Admin')
driver.find_element(By.NAME,"password").send_keys('admin123')
driver.find_element(By.TAG_NAME, "button").click()
# not working
admin = driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']")
usermgmt= driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
users = driver.find_element(By.XPATH,"//a[normalize-space()='Users']")

# Mouse over
act = ActionChains(driver)

act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()
