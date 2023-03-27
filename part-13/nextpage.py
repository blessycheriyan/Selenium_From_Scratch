from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# import KEYS
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
# driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
# Opening a new window registers page 
# register_new_page = Keys.CONTROL + Keys.RETURN
# driver.find_element(By.XPATH,"//a[normalize-space()='Register']").send_keys(register_new_page )
# open a new page or new browser

driver.get('https://demo.nopcommerce.com/')
# driver.switch_to.new_window('tab')
# driver.switch_to.new_window('window')
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


# cookeis 
cookies = driver.get_cookies()
print("Size of the cookie:",len(cookies))

# All cookeis 

for cookie in cookies:
    # print("Cookie:",cookie)
    print(cookie.get('name'),"",cookie.get('value'))
    
# Add new cookiesin the browser
driver.add_cookie({"name":'MyCookie','value':'12345'})   
cookies = driver.get_cookies()
print("Size of the cookie After:",len(cookies)) 

# Delete specific cookies in the browser
driver.delete_cookie('MyCookie')
cookies = driver.get_cookies()
print("Size of the cookie After deleted:",len(cookies)) 

# Delete all cookies in the browser
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of the cookie After deleted all cookies:",len(cookies)) 