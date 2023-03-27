from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import xlutilis
driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()
file= 'D:\Selenium\student_marks.xlsx'
rows = xlutilis.getrowcount()

for r in range(2,rows +1):
    pric = xlutilis.readData(file,'student_marks,r,1)
    rateofinterest = xlutilis.readData(file,'student_marks,r,2)
    per1= xlutilis.readData(file,'student_marks,r,3)
    per2= xlutilis.readData(file,'student_marks,r,4)
    fre = xlutilis.readData(file,'student_marks,r,5)
    exp_max= xlutilis.readData(file,'student_marks,r,6)
    # passing the data to the 
    
    driver.find_element(By.XPATH, "Apply for vendor account").click()