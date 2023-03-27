from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# Pop the disable pop 
driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3')
driver.maximize_window()
driver.switch_to.frame("iframeResult")
field1= driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("welcome")

button1 = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")


# Mouse over
act = ActionChains(driver)

act.double_click(button1).perform() # double click 
