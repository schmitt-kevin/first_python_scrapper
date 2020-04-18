# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from fake_useragent import UserAgent

# import os
import time

chrome_Driver_path = 'C:\\Users\\ahswr\\OneDrive\\Documents\\chromedriver_win32\\chromedriver.exe'
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.headless = True
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
driver = webdriver.Chrome(chrome_Driver_path, options=chrome_options)


driver.get('need a website address')
# driver.get('https://www.chase.com/personal/credit-cards/login-account-access')
print(driver.title)
# time.sleep(5)
# driver.quit()