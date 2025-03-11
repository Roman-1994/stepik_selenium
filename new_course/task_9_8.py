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

    link_9_8_3 = 'https://parsinger.ru/expectations/6/index.html'
    link_9_8_4 = 'https://parsinger.ru/selenium/5.9/2/index.html'
    link_9_8_5 = 'https://parsinger.ru/selenium/5.9/3/index.html'
    link_9_8_6 = 'https://parsinger.ru/selenium/5.9/4/index.html'
    link_9_8_7 = 'https://parsinger.ru/selenium/5.9/5/index.html'
    link_9_8_8 = 'https://parsinger.ru/selenium/5.9/6/index.html'
    link_9_8_9 = 'https://parsinger.ru/selenium/5.9/7/index.html'
    

    try:
        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless=new')
        browser = webdriver.Chrome()#options=options)
        browser.get(link_9_8_9)
        browser.implicitly_wait(3)
        
        #task_9_8_3
        # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
        # res = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "BMH21YY"))).text
        # print(res)
        
        #task_9_8_4
        # WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.ID, "qQm9y1rk"))).click()
        # print(browser.switch_to.alert.text)
        
        #task_9_8_5
        # ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB',
        #            'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I', 'jolHZqD1', 'ZM6Ms3tw',
        #            '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

        # for id_ in ids_to_find:
        #     WebDriverWait(browser, 120).until(EC.visibility_of_element_located((By.ID, id_))).click()

        # print(browser.switch_to.alert.text)
        
        #task_9_8_6
        # browser.find_element(By.CSS_SELECTOR, 'span.close').click()
        # locator = (By.ID, 'ad')
        # WebDriverWait(browser, 10).until(EC.invisibility_of_element_located(locator))
        # browser.find_element(By.TAG_NAME, 'button').click()
        # print(browser.find_element(By.ID, 'message').text)
        
        #task_9_8_7
        # res = []
        # elems = browser.find_elements(By.CSS_SELECTOR, 'div.box_button')
        # for elem in elems:
        #     elem.click()
        #     browser.find_element(By.ID, 'close_ad').click()
        #     locator = (By.ID, 'ad_window')
        #     if WebDriverWait(browser, 10).until(EC.invisibility_of_element_located(locator)):
        #         WebDriverWait(browser, 10).until(lambda _: elem.text != '')
        #         res.append(elem.text)
        # print('-'.join(res))
        
        #task_9_8_8
        # elem = browser.find_element(By.ID, 'myCheckbox')
        # if WebDriverWait(browser, 10).until(EC.element_to_be_selected(elem)):
        #     browser.find_element(By.TAG_NAME, 'button').click()
        #     print(browser.find_element(By.ID, 'result').text)
        
        #task_9_8_9
        elems = browser.find_elements(By.CSS_SELECTOR, 'div.container')
        for elem in elems:
            elem_input = elem.find_element(By.TAG_NAME, 'input')
            if WebDriverWait(browser, 20).until(EC.element_to_be_selected(elem_input)):
                elem.find_element(By.TAG_NAME, 'button').click()
        print(browser.find_element(By.ID, 'result').text)
                
    
    finally:
        browser.quit()