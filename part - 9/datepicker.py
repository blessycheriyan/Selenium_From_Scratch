from optparse import Option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/datepicker/')
driver.maximize_window()
driver.switch_to.frame(0) # switch to frame
# driver.find_element(By.XPATH, "//*[@id='datepicker']").click()

year = "2024"
month = "March"
date = "30"
driver.find_element(By.XPATH, "//*[@id='datepicker']").click()
while True:
    mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    
    if mon == month and yr == year :
        print(mon,yr)
        break;
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click() # next arrow
        
        
 # select the date picker
 
dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//tr/td/a") # next arrow
for ele in dates:
    if ele.text == date:
        ele.click()
        break        
        
# calender scraping for dates picker 