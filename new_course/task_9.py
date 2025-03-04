from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, NoAlertPresentException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.color import Color
import time
import pytest
import re

def test_button_start():

    link_9_1_6 = 'https://parsinger.ru/selenium/9/9.1.1/index.html'
    link_9_2_2 = 'https://parsinger.ru/selenium/9/9.2.1/index.html'
    link_9_3_3 = 'http://parsinger.ru/selenium/9/9.3.1/index.html'
    link_9_4_4 = 'https://parsinger.ru/selenium/9/9.4.3/index.html'
    link_9_4_5 = 'https://parsinger.ru/selenium/9/9.4.4/index.html'
    link_9_4_6 = 'http://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html'
    link_9_4_8 = 'https://parsinger.ru/selenium/9/9.4.2/index.html'
    link_9_5_3 = 'https://parsinger.ru/selenium/9/9.5.1/index.html'
    

    try:
        #options = webdriver.ChromeOptions()
        #options.add_argument('window-size=1920x1080')
        #options.add_argument('--headless=new')
        browser = webdriver.Chrome()#options=options)
        browser.maximize_window()
        browser.get(link_9_5_3)
        browser.implicitly_wait(10)
        
        #task_9_1_6
        # for i in range(1, 5):
        #     elem = browser.find_element(By.ID, f'button{i}')
        #     WebDriverWait(browser, 30).until(EC.element_to_be_clickable(elem)).click()
        # browser.find_element(By.ID, 'finalButton').click()
        # print(browser.find_element(By.ID, 'message').text)
        # print(browser.find_element(By.ID, 'message2').text)
        
        #task_9_2_2
        # browser.find_element(By.ID, 'startScan').click()
        # if WebDriverWait(browser, 30).until(EC.title_is('Access Granted')):
        #     print(browser.find_element(By.ID, 'passwordValue').text)
        
        #task_9_3_3
        # browser.find_element(By.ID, 'startButton').click()
        # for i in range(5):
        #     browser.find_element(By.ID, 'dynamicButton').click()
        # print(browser.find_element(By.ID, 'secretPassword').text)
        
        #task_9_4_4 
        # browser.find_element(By.XPATH, "(//div[@class='button-container']/a)[5]").click()
        # if WebDriverWait(browser, 10).until(EC.url_to_be('https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure')):
        #     print(browser.find_element(By.ID, 'password').text)
        
        #task_9_4_6
        # while True:
        #     try:
        #         browser.find_element(By.ID, 'searchLink').click()
        #         WebDriverWait(browser, 5).until(EC.url_contains('qLChv49'))
        #         break
        #     except TimeoutException:
        #         continue
        # browser.find_element(By.ID, 'checkButton').click()
        # print(browser.find_element(By.ID, 'result').text)
        
        #task_9_4_5
        # browser.find_element(By.CSS_SELECTOR, 'a.btn').click()
        # url = browser.current_url
        # while True:
        #     try:
        #         WebDriverWait(browser, 10).until(EC.url_changes(url))
        #         print(browser.find_element(By.ID, 'password').text)
        #         break
        #     except TimeoutException:
        #         continue
        
        #task_9_4_8
        # pattern = r'^https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html$'
        # browser.find_element(By.ID, 'startButton').click()
        # out = 0
        # while "index_2" not in browser.current_url:
        #     try:
        #         WebDriverWait(browser, poll_frequency=0.5,timeout=1).until(EC.url_matches(pattern))
        #         out += int(browser.find_element(By.CLASS_NAME,'number').text)
        #         time.sleep(1)
        #     except:
        #         pass
        # browser.find_element(By.ID,'sumInput').send_keys(out)
        # browser.find_element(By.ID, 'checkButton').click()
        # print(browser.find_element(By.ID, 'result').text)
        
        #task_9_5_3
        #if WebDriverWait(browser, poll_frequency=0.5,timeout=10).until(EC.visibility_of_element_located((By.ID, 'order-number'))):
        if WebDriverWait(browser, poll_frequency=0.5,timeout=10).until(EC.presence_of_element_located((By.ID, 'order-number'))):
            print(browser.find_element(By.ID, 'order-number').text)
        # if WebDriverWait(browser, poll_frequency=0.5,timeout=1000).until(EC.visibility_of_element_located((By.ID, 'loading-text'))):
        #     print(browser.find_element(By.ID, 'loading-text').text)
        # time.sleep(200)
        
        
    finally:
        browser.quit()