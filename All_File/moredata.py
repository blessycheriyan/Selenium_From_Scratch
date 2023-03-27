from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# driver.get('http://automationpractice.pl/index.php?controller=authentication&back=my-account')
# driver.maximize_window()
driver.get('http://automationpractice.pl/')
driver.maximize_window()
# slider = driver.find_elements(By.CLASS_NAME, "homeslider-container")
# print(len(slider)) # total number of sliders - 5
# links = driver.find_elements(By.TAG_NAME, "a")
# print(len(links)) # total links of sliders on homepage  - 95
# tag & Id = #
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("bless")
# tag & class name = .
# driver.find_element(By.CSS_SELECTOR, "input.is_required").send_keys("bless")
# driver.find_element(By.CSS_SELECTOR, ".is_required").send_keys("bless")
# tag & attribute = []
# driver.find_element(By.CSS_SELECTOR, "input[data-validate]").send_keys("bless")
# driver.find_element(By.CSS_SELECTOR, "[data-validate]").send_keys("bless")
# tag & class & attribute = #.[]
# driver.find_element(By.CSS_SELECTOR, "input.is_required[data-validate]").send_keys("bless")

# Absoulte -Full Xpath

# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirt")
# button xpath and click to search
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

# Relative -partial Xpath
# driver.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//*[@id='searchbox']/button").click()
# OR
# driver.find_element(By.XPATH, "//input[@id ='search_query_top' or name ='search_query']").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//button[@name ='submit_search' or class ='btn btn-default button-search']" ).click()

# Contains & start-with
# driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("T-shirt")
# # driver.find_element(By.XPATH, "//button[contains(@name ,'submit')]").click()
# driver.find_element(By.XPATH, "//button[starts-with(@name ,'submit_')]").click()

# text() //clicking on the link
driver.find_element(By.XPATH, "//a[text()='Women']").click()