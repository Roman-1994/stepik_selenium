from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, NoAlertPresentException
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
    

    try:
        #options = webdriver.ChromeOptions()
        #options.add_argument('window-size=1920x1080')
        #options.add_argument('--headless=new')
        browser = webdriver.Chrome()#options=options)
        browser.maximize_window()
        browser.get(link_9_3_3)
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
        browser.find_element(By.ID, 'startButton').click()
        for i in range(5):
            browser.find_element(By.ID, 'dynamicButton').click()
        print(browser.find_element(By.ID, 'secretPassword').text)
        
        
    finally:
        browser.quit()