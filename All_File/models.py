from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://money.rediff.com/losers/bse/daily/groupall')
driver.maximize_window()
# self
# text_msg =  driver.find_element(By.XPATH, "//a[contains(text(),'Jetmall Spices')]/self::a").text
# print(text_msg)

# parent
# text_msg =  driver.find_element(By.XPATH, "//a[contains(text(),'Jetmall Spices')]/parent::td").text
# print(text_msg)

# child
# text_msg =  driver.find_element(By.XPATH, "//a[contains(text(),'Jetmall Spices')]/ancestor::tr/child::td").text
# print(text_msg)

# child - Multiple elements case
# text_msg =  driver.find_elements(By.XPATH, "//a[contains(text(),'Jetmall Spices')]/ancestor::tr/child::td")
# print(len(text_msg))

 # ancestor
# text_msg =  driver.find_element(By.XPATH, "//a[contains(text(),'Jetmall Spices')]/ancestor::tr").text
# print(text_msg)

# descentor
# text_msg =  driver.find_elements(By.XPATH, "//a[contains(text(),'Jetmall Spices')]/ancestor::tr/descendant::*")
# print(len(text_msg))

# Following
# text_msg =  driver.find_elements(By.XPATH, "//a[contains(text(),'Jetmall Spices')]/ancestor::tr/following::*")
# print(len(text_msg))

# Following-sibling (subset of following)
# text_msg =  driver.find_elements(By.XPATH, "//a[contains(text(),'Jetmall Spices')]/ancestor::tr/following-sibling::*")
# print(len(text_msg))

# Preceding
# text_msg =  driver.find_elements(By.XPATH, "//a[contains(text(),'Jetmall Spices')]/ancestor::tr/preceding::*")
# print(len(text_msg))

# Preceding -sibling
text_msg =  driver.find_elements(By.XPATH, "//a[contains(text(),'Jetmall Spices')]/ancestor::tr/preceding-sibling::tr")
print(len(text_msg))
# driver.close()
