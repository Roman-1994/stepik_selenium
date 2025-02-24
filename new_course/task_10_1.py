from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import re

def test_button_start():

    link_10_1_6 = 'https://parsinger.ru/draganddrop/1/index.html'
    link_10_1_7 = 'https://parsinger.ru/draganddrop/3/index.html'
    

    try:
        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless=new')
        browser = webdriver.Chrome()#options=options)
        browser.get(link_10_1_7)
        browser.implicitly_wait(3)
        
        #task_10_1_6
        # elem = browser.find_element(By.ID, 'draggable')
        # target = browser.find_element(By.ID, 'field2')
        # action = ActionChains(browser)
        # action.drag_and_drop(elem, target).perform()
        # print(browser.find_element(By.ID, 'result').text)
        
        #task_10_1_7
        elem = browser.find_element(By.ID, 'block1')
        action = ActionChains(browser)
        action.click_and_hold(elem).perform()
    
        for i in range(1, 6):
            target = browser.find_element(By.ID, f'point{i}')  
            action.move_to_element(target) 
        
        action.release().perform()
        WebDriverWait(browser, 30).until(lambda x: len(browser.find_element(By.ID, 'message').text) > 0)
        print(browser.find_element(By.ID, 'message').text)
    
    finally:
        browser.quit()