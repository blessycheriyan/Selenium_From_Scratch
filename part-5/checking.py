
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.ebay.com/')
driver.maximize_window()
driver.find_element(By.NAME,"_nkw").send_keys("Watch")
driver.find_element(By.NAME,"_nkw").send_keys(Keys.ENTER)

watch_= driver.find_elements(By.CLASS_NAME,"s-item__title")
# watch_ names full 
for w in watch_:
    print(w.text)


