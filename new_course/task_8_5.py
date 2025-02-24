from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, NoAlertPresentException
import time
import pytest
import re

def test_button_start():

    link_8_5_1 = 'https://parsinger.ru/selenium/5.8/1/index.html'
    link_8_5_2 = 'https://parsinger.ru/selenium/5.8/2/index.html'
    link_8_5_3 = 'https://parsinger.ru/selenium/5.8/3/index.html'
    link_8_5_4 = 'http://parsinger.ru/window_size/1/'
    link_8_5_5 = 'http://parsinger.ru/window_size/2/index.html'
    link_8_5_7 = 'http://parsinger.ru/blank/3/index.html'
    link_8_5_8 = ['http://parsinger.ru/blank/1/1.html', 
                  'http://parsinger.ru/blank/1/2.html', 
                  'http://parsinger.ru/blank/1/3.html', 
                  'http://parsinger.ru/blank/1/4.html', 
                  'http://parsinger.ru/blank/1/5.html', 
                  'http://parsinger.ru/blank/1/6.html',]
    link_8_5_9 = 'https://parsinger.ru/selenium/5.8/5/index.html'
    

    try:
        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless=new')
        browser = webdriver.Chrome()#options=options)
        browser.get(link_8_5_9)
        browser.implicitly_wait(3)
        
        
        #task_8_5_1
        # elems = browser.find_elements(By.CLASS_NAME, 'buttons')
        # for elem in elems:
        #     elem.click()
        #     browser.switch_to.alert.accept()
        #     if browser.find_element(By.ID, 'result').text != '':
        #         print(browser.find_element(By.ID, 'result').text)
        #         break
        
        #task_8_5_2
        # elems = browser.find_elements(By.CLASS_NAME, 'buttons')
        # for elem in elems:
        #     elem.click()
        #     res = browser.switch_to.alert.text
        #     browser.switch_to.alert.accept()
        #     browser.find_element(By.ID, 'input').send_keys(res)
        #     browser.find_element(By.ID, 'check').click()
        #     if browser.find_element(By.ID, 'result').text != 'Неверный пин-код':
        #         print(browser.find_element(By.ID, 'result').text)
        #         break
        
        #task_8_5_3
        # elems = browser.find_elements(By.TAG_NAME, 'span')
        # for elem in elems:
        #     pin = elem.text
        #     browser.find_element(By.ID, 'check').click()
        #     browser.switch_to.alert.send_keys(pin)
        #     browser.switch_to.alert.accept()
        #     if browser.find_element(By.ID, 'result').text != 'Неверный пин-код':
        #         print(browser.find_element(By.ID, 'result').text)
        #         break
        
        #task_8_5_4
        # for i in range(150):
        #     for j in range(150):
        #         browser.set_window_size(555+i, 555+j)
        #         if browser.find_element(By.ID, 'result').text != '':
        #             break
        #     if browser.find_element(By.ID, 'result').text != '':
        #         print(browser.find_element(By.ID, 'result').text)
        #         break
        
        #task_8_5_5
        # window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
        # window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
        # for i in window_size_x:
        #     for j in window_size_y:
        #         browser.set_window_size(i+16, j+147)
        #         #time.sleep(3)
        #         try: 
        #             res = browser.find_element(By.ID, 'result').text
        #             if res:
        #                 print(res)
        #                 break
        #         except:
        #             continue
        
        #task_8_5_6
        # window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
        # window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
        # for i in window_size_x:
        #     for j in window_size_y:
        #         browser.set_window_size(i+16, j+147)
        #         #time.sleep(3)
        #         try: 
        #             res = browser.find_element(By.ID, 'result').text
        #             if res:
        #                 size = browser.get_window_size()
        #                 print(size)
        #                 break
        #         except:
        #             continue
        
        #task_8_5_7
        # res = []
        # elems = browser.find_elements(By.TAG_NAME, 'input')
        # for elem in elems:
        #     elem.click()
        #     browser.switch_to.window(browser.window_handles[-1])
        #     res.append(int(browser.title))
        #     browser.switch_to.window(browser.window_handles[0])
        # print(sum(res))
        
        #task_8_5_8
        # result = 0
        # for i in link_8_5_8:
        #     browser.get(i)
        #     browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        #     result += int(browser.find_element(By.ID, 'result').text) ** 0.5
        #     if i != link_8_5_8[-1]:
        #         browser.switch_to.new_window('tab')
        #     time.sleep(1)
        # print(round(result, 9))
        
        #task_8_5_9
        for i in range(1, 10):
            iframe = browser.find_element(By.ID, f'iframe{i}')
            browser.switch_to.frame(iframe)
            browser.find_element(By.TAG_NAME, 'button').click()
            elem = browser.find_element(By.ID, 'numberDisplay').text
            browser.switch_to.default_content()
            browser.find_element(By.ID, 'guessInput').clear()
            browser.find_element(By.ID, 'guessInput').send_keys(elem)
            browser.find_element(By.ID, 'checkBtn').click()
            time.sleep(2)
            try:
                print(browser.switch_to.alert.text)
            except:
                continue
        
        
    finally:
        browser.quit()