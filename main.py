from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
from secret import ACCOUNT_EMAIL, ACCOUNT_PASSWORD

chrome_driver_path = "C:\workspacePython\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.tinder.com")
driver.maximize_window()
time.sleep(2)
sign_in_button = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
sign_in_button.click()
time.sleep(2)
facebook_login = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_login.click()
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
user_facebook_login = driver.find_element_by_xpath('//*[@id="email"]')
user_facebook_login.send_keys(ACCOUNT_EMAIL)
pass_facebook_login = driver.find_element_by_xpath('//*[@id="pass"]')
pass_facebook_login.send_keys(ACCOUNT_PASSWORD)
pass_facebook_login.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
time.sleep(4)
location_cookies = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[1]/span')
location_cookies.click()
time.sleep(4)
notification_denied_cookies = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[2]/span')
notification_denied_cookies.click()
time.sleep(4)
acept_cookies = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[2]/div/div/div[1]/button/span')
acept_cookies.click()
for n in range(100):
    time.sleep(4)
    # like_button = driver.find_element_by_xpath(
    #     '//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
    # like_button.click()
    try:
        like_button = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_xpath('//*[@id="c155633096"]/div/div/div[1]/div/div[4]/button')
            match_popup.click()
        except NoSuchElementException:
            question_popup = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div[2]/button[2]')
            question_popup.click()

            time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)



