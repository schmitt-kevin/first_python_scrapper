# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from fake_useragent import UserAgent

# import os
import config #import the config file data
import time

chrome_Driver_path = 'C:\\Users\\ahswr\\OneDrive\\Documents\\chromedriver_win32\\chromedriver.exe'
pw = config.CHASE_PW
un = config.CHASE_UN
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.headless = True
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("--window-size=1920x1080")
# chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

# using windows file path
# using double backslashes to exit the first backslashes
# driver = webdriver.Chrome(executable_path=chrome_Driver_path, options=chrome_options,  service_args=['--verbose', '--log-path=/tmp/logs/chromedriver.log'])
driver = webdriver.Chrome(chrome_Driver_path, options=chrome_options)


driver.get('https://secure03a.chase.com/web/auth/dashboard#/dashboard/overviewAccounts/overview/index')
# driver.get('https://www.chase.com/personal/credit-cards/login-account-access')
print(driver.title)
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.jpui.input.logon-xs-toggle.clientSideError"))).send_keys(un)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signin-button"]')))

# myDynamicElement = driver.find_element_by_id("userId-text-input-field")
# driver.find_element_by_css_selector("input.jpui.input.logon-xs-toggle#password-input-field").send_keys("hello")
# driver.find_element_by_css_selector("button#signin-button>span.label").click()
# time.sleep(5)
# html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
# print(html)
# time.sleep(3)
# /html/body/div/div[1]/div[3]/main/div/div[2]/div[2]/div/div[2]/div/form/div[1]/div/div[1]/div[2]/input
# //*[@id="userId-text-input-field"]
driver.find_element_by_xpath("//*[@id='userId-text-input-field']").send_keys(un)
# driver.find_element_by_xpath('//*[@id="userId-text-input-field"]').send_keys(un)
# //*[@id="password-text-input-field"]
driver.find_element_by_xpath('//*[@id="password-text-input-field"]').send_keys(pw)
# //*[@id="signin-button"]
driver.find_element_by_xpath('//*[@id="signin-button"]').submit()
print(driver.title)
driver.quit()