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

    link_8_1_3_1 = 'https://parsinger.ru/selenium/8/8.1/site1/'
    link_8_1_3_2 = 'https://parsinger.ru/selenium/8/8.1/site2/'
    link_8_1_8 = 'https://parsinger.ru/selenium/8/8.1.2/index.html'
    link_8_2_4 = 'https://parsinger.ru/selenium/8/8.2.1/index.html'
    link_8_2_6 = 'https://parsinger.ru/selenium/8/8.2.2/index.html'
    link_8_3_5 = 'https://parsinger.ru/selenium/8/8.3.1/index.html'
    link_8_4_4 = 'https://parsinger.ru/selenium/8/8.4.1/'
    link_8_4_5 = 'https://parsinger.ru/selenium/8/8.4.2/index.html'
    link_8_4_6 = 'https://parsinger.ru/selenium/8/8.4.3/index.html'
    

    try:
        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless=new')
        browser = webdriver.Chrome()#options=options)
        browser.maximize_window()
        browser.get(link_8_4_6)
        browser.implicitly_wait(3)
        
        #task_8_1_3
        # browser.switch_to.new_window('tab')
        # browser.get(link_8_1_3_1)
        # title_1 = int(browser.title.replace('4', '').replace('3', '').replace('9', ''))
        
        # browser.switch_to.new_window('tab')
        # browser.get(link_8_1_3_2)
        # title_2 = int(browser.title.replace('7', '').replace('8', '').replace('0', ''))
        
        # print(title_1 + title_2)
        
        #task_8_1_8
        # result = 0
        # elems = browser.find_elements(By.TAG_NAME, 'a')
        # elems = list(map(lambda x: x.get_attribute('href'), elems))
        # #print(list(elems))
        # for elem in elems:
        #     browser.switch_to.new_window('tab')
        #     browser.get(elem)
        #     time.sleep(4)
        #     result += sum(map(lambda x: int(x.text), browser.find_elements(By.CLASS_NAME, 'number')))
        # browser.switch_to.window(browser.window_handles[0])
        # browser.find_element(By.ID, 'sumInput').send_keys(result)
        # browser.find_element(By.ID, 'checkButton').click()
        # print(browser.find_element(By.ID, 'passwordDisplay').text)
        
        #task_8_2_4
        # browser.set_window_size(1200, 720)
        # browser.find_element(By.ID, 'checkSizeBtn').click()
        # print(browser.find_element(By.ID, 'secret').text)
        
        #task_8_2_6
        # browser.find_element(By.ID, 'answer').send_keys(browser.get_window_size()["width"] + browser.get_window_size()["height"])
        # browser.find_element(By.ID, 'checkBtn').click()
        # print(browser.find_element(By.ID, 'resultMessage').text)
        
        #task_8_3_5
        # browser.find_element(By.ID, 'alertButton').click()
        # browser.switch_to.alert.accept()
        # time.sleep(2)
        # browser.find_element(By.ID, 'promptButton').click()
        # browser.switch_to.alert.send_keys('Alert')
        # browser.switch_to.alert.accept()
        # time.sleep(2)
        # browser.find_element(By.ID, 'confirmButton').click()
        # browser.switch_to.alert.accept()
        # time.sleep(2)
        # print(browser.find_element(By.CLASS_NAME, 'secret-key').text)
        
        #task_8_4_4
        # frame = browser.find_element(By.TAG_NAME, 'iframe')
        # browser.switch_to.frame(frame)
        # text = browser.page_source
        # text = text.split('*')[1::2]
        # print(''.join(text))
        
        #task_8_4_5
        # action = ActionChains(browser)
        # for i in range(1, 5):
        #     iframe = browser.find_element(By.ID, f'frame{i}')
        #     browser.switch_to.frame(iframe)
        #     browser.page_source
        #     if i < 4:
        #         browser.find_element(By.CLASS_NAME, 'unlock-button').click()
        #         browser.switch_to.default_content()
        #         action.key_down(Keys.END).key_up(Keys.END).perform()
        #     else:
        #         print(browser.find_element(By.TAG_NAME, 'h2').text)
        
        #task_8_4_6
        for i in range(1, 5):
            iframe = browser.find_element(By.TAG_NAME, 'iframe')
            browser.switch_to.frame(iframe)
            browser.page_source
            browser.find_element(By.CLASS_NAME, 'button').click()
            if i == 4:
                print(browser.find_element(By.CLASS_NAME, 'password-container').text)
                        
        
    finally:
        browser.quit()