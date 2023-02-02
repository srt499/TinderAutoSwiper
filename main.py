from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "C:\python\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

driver.get("https://tinder.com/")
driver.maximize_window()

time.sleep(1)

login_button = driver.find_element(By.LINK_TEXT, 'Log in')
login_button.click()

time.sleep(1)

facebook_button = driver.find_element(By.XPATH, "//*[contains(@aria-label, 'Log in with Facebook')]")
facebook_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

time.sleep(1)

driver.switch_to.window(fb_login_window)
email = driver.find_element(By.ID, "email")
email.send_keys('Enter-facebook-email-here')
password = driver.find_element(By.ID, "pass")
password.send_keys('Enter-password-here')

facebook_login_button = driver.find_element(By.ID, 'loginbutton')
facebook_login_button.click()

driver.switch_to.window(base_window)

time.sleep(5)

location_allow = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Allow')]")
location_allow.click()

notifications = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Not interested')]")
notifications.click()

time.sleep(2)

for n in range(100):
    time.sleep(3)
    try:
        body = driver.find_element(By.CSS_SELECTOR, value='body')
        body.send_keys(Keys.ARROW_LEFT)
        print('disliked')
    except:
        time.sleep(2)
        print('failed')

driver.quit()
