from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# Pop the disable pop 
driver = webdriver.Chrome()
driver.get('https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/')

driver.maximize_window()

Slider_left_end =  driver.find_element(By.XPATH,"//span[1]")
Slider_right_end =  driver.find_element(By.XPATH,"//span[2]")

print(Slider_left_end.location)
print(Slider_right_end.location)

# Mouse over
act = ActionChains(driver)

act.drag_and_drop_by_offset(Slider_left_end,100,0).perform()
act.drag_and_drop_by_offset(Slider_right_end,-39,0).perform()

print("AFTER",Slider_left_end.location)
print("AFTER",Slider_right_end.location)