from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
country_list = driver.find_elements(By.XPATH,"//span[@class='select2-results']/ul/li")
print(len(country_list))

for country in country_list:
    if country.text == 'Australia' :
        print(country.text)
        country.click()
        break