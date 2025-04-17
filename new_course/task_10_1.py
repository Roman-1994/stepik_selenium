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

    link_10_1_6 = 'https://parsinger.ru/draganddrop/1/index.html'
    link_10_1_7 = 'https://parsinger.ru/draganddrop/3/index.html'
    link_10_1_8 = 'https://parsinger.ru/selenium/5.10/2/index.html'
    link_10_1_9 = 'https://parsinger.ru/draganddrop/2/index.html'
    link_10_1_10 = 'https://parsinger.ru/selenium/5.10/3/index.html'
    link_10_1_11 = 'https://parsinger.ru/selenium/5.10/4/index.html'
    link_10_1_12 = 'https://parsinger.ru/selenium/5.10/8/index.html'
    link_10_1_13 = 'https://parsinger.ru/selenium/5.10/6/index.html'
    

    try:
        #options = webdriver.ChromeOptions()
        #options.add_argument('window-size=1920x1080')
        #options.add_argument('--headless=new')
        browser = webdriver.Chrome()#options=options)
        browser.maximize_window()
        browser.get(link_10_1_13)
        browser.implicitly_wait(3)
        
        #task_10_1_6
        # elem = browser.find_element(By.ID, 'draggable')
        # target = browser.find_element(By.ID, 'field2')
        # action = ActionChains(browser)
        # action.drag_and_drop(elem, target).perform()
        # print(browser.find_element(By.ID, 'result').text)
        
        #task_10_1_7
        # elem = browser.find_element(By.ID, 'block1')
        # action = ActionChains(browser)
        # action.click_and_hold(elem).perform()
    
        # for i in range(1, 6):
        #     target = browser.find_element(By.ID, f'point{i}')  
        #     action.move_to_element(target) 
        
        # action.release().perform()
        # WebDriverWait(browser, 30).until(lambda x: len(browser.find_element(By.ID, 'message').text) > 0)
        # print(browser.find_element(By.ID, 'message').text)
        
        #task_10_1_8
        # action = ActionChains(browser)
        # end_elem = browser.find_element(By.CLASS_NAME, 'draganddrop_end')
        # for i in range(1, 11):
        #     elem = browser.find_element(By.ID, f'draganddrop{i}')
        #     action.drag_and_drop(elem, end_elem).perform()
        #     time.sleep(1)
        # print(browser.find_element(By.ID, 'message').text)
        
        #task_10_1_9
        # action = ActionChains(browser)
        # for i in range(1, 5):
        #     elem = browser.find_element(By.ID, 'draggable')
        #     end_elem = browser.find_element(By.ID, f'box{i}')
        #     action.drag_and_drop(elem, end_elem).perform()
        #     time.sleep(1)
        # print(browser.find_element(By.ID, 'message').text)
        
        #task_10_1_10
        # action = ActionChains(browser)
        # elems = browser.find_elements(By.CLASS_NAME, 'draganddrop')
        # elems_end = browser.find_elements(By.CLASS_NAME, 'draganddrop_end')
        # for elem in elems:
        #     for elem_end in elems_end:
        #         if Color.from_string(elem.value_of_css_property('background-color')).rgb == Color.from_string(elem_end.value_of_css_property('border-color')).rgb:
        #             action.drag_and_drop(elem, elem_end).perform()
        #             time.sleep(1)
        #             break
        # print(browser.find_element(By.ID, 'message').text)
        
        #task_10_1_11
        # action = ActionChains(browser)
        # balls = browser.find_elements(By.CLASS_NAME, 'ball_color')
        # baskets = browser.find_elements(By.CLASS_NAME, 'basket_color')
        # for ball in balls:
        #     for basket in baskets:
        #         if Color.from_string(ball.value_of_css_property('background-color')).rgb == Color.from_string(basket.value_of_css_property('background-color')).rgb:
        #             action.drag_and_drop(ball, basket).perform()
        #             time.sleep(1)
        #             break
        # print(browser.find_element(By.CLASS_NAME, 'message').text)
        
        #task_10_1_12
        # action = ActionChains(browser)
        # for i in range(100, 900, 100):
        #     elem = browser.find_element(By.ID, f'piece_{i}')
        #     elem_end = browser.find_element(By.ID, f'range_{i}')
        #     action.drag_and_drop(elem, elem_end).perform()
        #     time.sleep(1)
        # print(browser.find_element(By.ID, 'message').text)
        
        #task_10_1_13
        # sliders = browser.find_elements(By.CLASS_NAME, 'volume-slider')
        # target = browser.find_elements(By.CLASS_NAME, 'target-value')
        # for i in range(10):
        #     slider_value = int(sliders[i].get_attribute('value'))
        #     target_value = int(target[i].text)
        #     delta = slider_value - target_value
        #     if delta < 0:
        #         delta *= -1
        #         for j in range(1, delta + 1):
        #             sliders[i].send_keys(Keys.ARROW_RIGHT)
        #     elif delta == 0:
        #         continue
        #     elif delta > 0:
        #         for j in range(1, delta + 1):
        #             sliders[i].send_keys(Keys.ARROW_LEFT)
        #     time.sleep(1)
        # print(browser.find_element(By.ID, 'message').text)
        
        print('hello')
    
    finally:
        browser.quit()