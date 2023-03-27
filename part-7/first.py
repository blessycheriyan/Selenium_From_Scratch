import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://itera-qa.azurewebsites.net/home/automation')
driver.maximize_window()
# Select Specific Checkbox single Element
# search_box = driver.find_element(By.XPATH, "//input[@id='monday']").click()
# Select Specific Checkbox Multiple Element

check_box = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(check_box))
# Approach 1

# for i in range(len(check_box)):
#     check_box[i].click()
# Approach 2

for i in check_box:
    i.click()
# # Select the multiple checkbox by choice    
# for i in check_box:
#     week_name = i.get_attribute('id')
#     if week_name == 'monday' or week_name == 'saturday':
#         i.click()

# Select the 2 last checkbox 
# range(5,7) --> 6,7
# totalnumberelements  -2 =startingelement

# for i in range(len(check_box)-2,len(check_box)) :
#         check_box[i].click()
# Select the 2 first checkbox 
# for i in range(len(check_box)) :
#     if i < 2:
#         check_box[i].click()
# Clearing all the checkboxes

time.sleep(3)
for i in  check_box:
    if i.is_selected():
        i.click()
