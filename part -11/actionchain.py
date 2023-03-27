from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# Pop the disable pop 

driver = webdriver.Chrome()
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()
button = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

# Mouse over
act = ActionChains(driver)

act.context_click(button).perform() # right click 
time.sleep(5)
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()

driver.switch_to.alert.accept()