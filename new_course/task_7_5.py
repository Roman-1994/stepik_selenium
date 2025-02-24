from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
import time
import pytest
import re

def test_button_start():

    link_7_5_1 = 'http://parsinger.ru/scroll/2/index.html'
    link_7_5_2 = 'http://parsinger.ru/infiniti_scroll_1/'
    link_7_5_3 = 'http://parsinger.ru/infiniti_scroll_2/'
    link_7_5_4 = 'http://parsinger.ru/infiniti_scroll_3/'
    link_7_5_5 = 'https://parsinger.ru/selenium/5.7/1/index.html'
    link_7_5_6 = 'https://parsinger.ru/selenium/5.7/5/index.html'
    link_7_5_7 = 'https://parsinger.ru/selenium/5.7/4/index.html'
    link_7_5_8 = 'https://parsinger.ru/selenium/7/7.5/index.html'
    

    try:
        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless=new')
        browser = webdriver.Chrome()#options=options)
        browser.get(link_7_5_8)
        browser.implicitly_wait(3)
        
        #task_7_5_1
        # result = 0
        # elems = browser.find_elements(By.CSS_SELECTOR, 'div.item')
        # for elem in elems:
        #     elem.find_element(By.TAG_NAME, 'input').click()
        #     if str(elem.find_element(By.TAG_NAME, 'span').text).isdigit():
        #         result += int(elem.find_element(By.TAG_NAME, 'span').text)
        # print(result)
        
        #task_7_5_2
        # result = 0
        # action = ActionChains(browser)
        # browser.find_element(By.CSS_SELECTOR, 'div[id=scroll-wrapper] > div:nth-child(1)').click()
        # while True:
        #     try:
        #         browser.find_element(By.CLASS_NAME, 'last-of-list').is_displayed()
        #         action.key_down(Keys.END).key_up(Keys.END).perform()
        #         break
        #     except NoSuchElementException:
        #         action.key_down(Keys.END).key_up(Keys.END).perform()
        #         time.sleep(2)
            
        # elems_span = browser.find_elements(By.TAG_NAME, 'span')
        # for elem in elems_span:
        #     if elem.text.isdigit():
        #         result += int(elem.text)
            
        # print(result)
        
        #task_7_5_3
        # result = 0
        # action = ActionChains(browser)
        # browser.find_element(By.CSS_SELECTOR, 'div[id=scroll-wrapper] > div:nth-child(1)').click()
        # while True:
        #     if len(browser.find_elements(By.CSS_SELECTOR, 'div[id=scroll-wrapper] > div:nth-child(1) > p')) < 100:
        #         action.key_down(Keys.END).key_up(Keys.END).perform()
        #         time.sleep(2)
        #     else:
        #         break
            
        # elems_p = browser.find_elements(By.CSS_SELECTOR, 'div[id=scroll-wrapper] > div:nth-child(1) > p')
        # for elem in elems_p:
        #     if elem.text.isdigit():
        #         result += int(elem.text)
        # print(result)
        
        #task_7_5_4
        # result = 0
        # action = ActionChains(browser)
        # for i in range(1, 6):
        #     browser.find_element(By.CSS_SELECTOR, f'div.scroll-container_{i}').click()
        #     while True:
        #         if len(browser.find_elements(By.CSS_SELECTOR, f'div.scroll-container_{i} span')) < 100:
        #             action.key_down(Keys.END).key_up(Keys.END).perform()
        #             time.sleep(2)
        #         else:
        #             break
        #     elems_span = browser.find_elements(By.CSS_SELECTOR, f'div.scroll-container_{i} span')
        #     for elem in elems_span:
        #         if elem.text.isdigit():
        #             result += int(elem.text)
        # print(result)
        
        #task_7_5_5
        # buttons = browser.find_elements(By.CLASS_NAME, 'clickMe')
        # for button in buttons:
        #     browser.execute_script('return arguments[0].scrollIntoView(true)', button)
        #     button.click()
        # print(browser.switch_to.alert.text)
        
        #task_7_5_6
        # action = ActionChains(browser)
        # for i in range(1, 5):
        #     button = browser.find_element(By.ID, f'button{i}')
        #     time_button = float(button.get_attribute('value'))
        #     action.click_and_hold(button).pause(time_button).release(button).perform()
        # print(browser.switch_to.alert.text)
        
        #task_7_5_7
        # browser.find_element(By.ID, 'main_container').click()
        # action = ActionChains(browser)
        # while True:
        #     if len(browser.find_elements(By.CLASS_NAME, 'child_container')) < 100:
        #         action.key_down(Keys.END).key_up(Keys.END).perform()
        #         time.sleep(1)
        #     else:
        #         break
        # elems = browser.find_elements(By.CLASS_NAME, 'child_container')
        # for elem in elems:
        #     elem_input = elem.find_elements(By.TAG_NAME, 'input')
        #     for inp in elem_input:
        #         if int(inp.get_attribute('value')) % 2 == 0:
        #             inp.click()
        # action.key_down(Keys.END).key_up(Keys.END).perform()
        # browser.find_element(By.CLASS_NAME, 'alert_button').click()
        # time.sleep(3)
        # print(browser.switch_to.alert.text)
        
        #task_7_5_8
        result = 0
        browser.find_element(By.ID, 'container').click()
        action = ActionChains(browser)
        while True:
            if len(browser.find_elements(By.CSS_SELECTOR, 'div.card div.like-container')) < 100:
                action.key_down(Keys.END).key_up(Keys.END).perform()
                time.sleep(1)
            else:
                break
        elems = browser.find_elements(By.CSS_SELECTOR, 'div.card div.like-container')
        for elem in elems:
            elem.find_element(By.CSS_SELECTOR, 'span.like-btn').click()
            result += int(elem.find_element(By.CSS_SELECTOR, 'span.big-number').text)
        print(result)
        
        
    finally:
        browser.quit()