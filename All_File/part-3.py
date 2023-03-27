from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://automationpractice.pl/index.php?controller=authentication&back=my-account')
driver.maximize_window()
# Absolute -Full Xpath

driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirt")
# button xpath and click to search
driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

# Relative -partial Xpath
# driver.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//*[@id='searchbox']/button").click()

# OR
# driver.find_element(By.XPATH, "//input[@id ='search_query_top' or name ='search_query']").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//button[@name ='submit_search' or class ='btn btn-default button-search']" ).click()

# Contains & start-with

# driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//button[contains(@name ,'submit')]").click()
# driver.find_element(By.XPATH, "//button[starts-with(@name ,'submit_')]").click()

# text() //clicking on the link
driver.find_element(By.XPATH, "//a[text()='Women']").click()
# driver.close()