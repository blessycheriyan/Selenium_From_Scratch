from optparse import Option
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()
driver.switch_to.frame(0) # switch to frame


# date pick
driver.find_element(By.XPATH, "//input[@id='dob']").click()

# datepicker_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))

# datepicker_month.select_by_visible_text('Dec')

# datepicker_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))

# datepicker_year.select_by_visible_text('1990')

# all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tr/td/a")

# for date in all_dates:
#     if date.text == 25:
#         print(datepicker_month,datepicker_year,date.text)
#         date.click()
#         break;



# not working this site----
    
    
    
    