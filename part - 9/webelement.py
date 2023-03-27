from optparse import Option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Pop the disable pop 
driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
# 1) count no of rows & columns 
no_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
no_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr//th"))  
# print(no_rows)
# print(no_columns)
# 2) Read Specific rows & columns 
# data= driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
# print(data)
# 3) Read all rows & columns 
# for r in range(2, no_rows+1):
#     for c in range(1, no_columns+1):

#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text

#         print(data,end='         ')
#     print()        

# 3) Read data based on the condition(List book name whose author is Mukesh)
for r in range(2, no_rows+1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]//td[2]").text
    if author_name == 'Mukesh':
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]//td[1]").text
        price_ = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]//td[4]").text
        print(author_name+ " " + book_name+ " " +price_)