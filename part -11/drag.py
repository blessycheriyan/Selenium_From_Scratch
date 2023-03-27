from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# Pop the disable pop 
driver = webdriver.Chrome()
driver.get('https://ui.vision/demo/webtest/dragdrop/')
driver.implicitly_wait(10)
driver.maximize_window()

drag1 =  driver.find_element(By.ID,"one")
target1  =  driver.find_element(By.ID,"bin")



# Mouse over
act = ActionChains(driver)

act.drag_and_drop(drag1,target1) .perform() # drag & drop 
