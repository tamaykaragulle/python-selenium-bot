from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

tc = ""
password = ''

browser = webdriver.Chrome()

browser.get('https://www.btkakademi.gov.tr/portal/sign-in?returnUrl=/'),
time.sleep(2)

browser.find_element('xpath','//*[@id="login"]/div[1]/p/button').click()
time.sleep(2)

tcInput = browser.find_element('xpath','//*[@id="tridField"]')
passwordInput = browser.find_element('xpath','//*[@id="egpField"]')

tcInput.send_keys(tc)
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.ENTER)
time.sleep(5)

browser.find_element('xpath','//*[@id="gbt_index-current-slider"]/div[2]/div[1]/div/div[1]/a').click()
time.sleep(5)

browser.find_element('xpath','//*[@id="container-toggle"]/div/div/div[1]/div[2]/div[1]/button').click()
time.sleep(5)

sections = browser.find_elements(By.CLASS_NAME,'sc-cjibBx')

for section in sections:
    videos = section.find_elements(By.CLASS_NAME,'sc-cabOPr')
    for video in videos:
        className = video.get_attribute('class')
        if "completed" in className:
            pass
        else:
            video.click()
            time.sleep(20)
