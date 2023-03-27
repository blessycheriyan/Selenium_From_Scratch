from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# Total number  of link
dropdwn= driver.find_element(By.XPATH,"//select[@id='input-country']")

drop_country = Select(dropdwn)
# select option from dropdown
drop_country.select_by_visible_text("India")

# # Another method - select option from dropdown
# drop_country.select_by_value(10)
# # Another method - select option from dropdown for index
# drop_country.select_by_index(13)
# capture all the options and print them

all_opt = drop_country.options
print("All options:",len(all_opt))

for option in all_opt:
    print("Option:",option.text)
    
# Select option from dropdown without using built function

for option in all_opt:
    if option.text == 'India':
        option.click()
        break

# Select option from dropdown without Select label assume
all_opt =driver.find_element(By.XPATH, '//*[@id="input-country"]/option')  
print(len(all_opt))
    