from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

def test_button_start():

    link_7_1_6 = 'https://parsinger.ru/selenium/7/7.1/index.html'
    link_7_2_5 = 'https://parsinger.ru/selenium/7/7.2/index.html'
    link_7_3_3 = 'http://parsinger.ru/selenium/7/7.3.1/index.html'
    link_7_3_7 = 'https://parsinger.ru/selenium/7/7.3.3/index.html'
    link_7_3_8 = 'https://parsinger.ru/selenium/7/7.3.4/index.html'
    link_7_3_9 = 'https://parsinger.ru/selenium/7/7.3.5/index.html'
    link_7_4_2 = 'https://parsinger.ru/selenium/7/7.4.1/index.html'
    

    try:
        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless=new')
        browser = webdriver.Chrome()#options=options)
        browser.get(link_7_4_2)
        browser.implicitly_wait(3)
        
        #task_7_1_6
        # height_body = browser.execute_script("return document.body.scrollHeight")
        # browser.execute_script(f'window.scrollTo(0, {height_body});')
        # time.sleep(3)
        # print(browser.find_element(By.ID, 'secret-container').text)
        
        #task_7_2_5
        #elems = browser.find_element(By.CLASS_NAME, 'interactive')
        # for i in range(1, 101):
        #     elems = browser.find_element(By.CSS_SELECTOR, f'div.input-container div.input-wrapper:nth-child({i}) .interactive')
        #     elems.send_keys('1')
        #     elems.send_keys(Keys.ENTER)
        #     elems.send_keys(Keys.ARROW_DOWN)
        #     browser.execute_script("return arguments[0].scrollIntoView(true);", elems)
        #     time.sleep(1)
        # print(browser.find_element(By.ID, 'hidden-password').text)
        
        #task_7_3_3
        # elem_sourse = browser.find_element(By.ID, 'draggable')
        # elem_target = browser.find_element(By.ID, 'target')
        # action = ActionChains(browser)
        # action.drag_and_drop(elem_sourse, elem_target).perform()
        # action.reset_actions()
        # print(browser.find_element(By.ID, 'password').text)
        
        #task_7_3_7
        # action = ActionChains(browser)
        # action.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).key_down('T').perform()
        # action.key_up(Keys.CONTROL).key_up(Keys.ALT).key_up(Keys.SHIFT).key_up('T').perform()
        # action.reset_actions()
        # print(browser.find_element(By.TAG_NAME, 'span').text)
        
        #task_7_3_8
        # elem = browser.find_element(By.ID, 'context-area')
        # action = ActionChains(browser)
        # action.context_click(elem).perform()
        # context_elem = browser.find_element(By.CSS_SELECTOR, '#custom-menu div:nth-child(3)')
        # action.click(context_elem).perform()
        # action.reset_actions()
        # print(browser.find_element(By.TAG_NAME, 'span').text)
        
        #task_7_3_9
        # action = ActionChains(browser)
        # left_elem = browser.find_element(By.ID, 'scrollable-container-left')
        # right_elem = browser.find_element(By.ID, 'scrollable-container-right')
        # action.click(left_elem).send_keys(Keys.END).perform()
        # time.sleep(3)
        # action.click(right_elem).send_keys(Keys.END).perform()
        # time.sleep(3)
        # action.reset_actions()
        # print(browser.find_element(By.TAG_NAME, 'span').text)
        # assert browser.find_element(By.TAG_NAME, 'span').text != '', 'ERROR'
        
        #task_7_4_2
        action = ActionChains(browser)
        action.scroll_by_amount(0, 500).perform()
        elem_1 = browser.find_element(By.CLASS_NAME, 'countdown')
        time.sleep(4)
        elem_1 = elem_1.text.split(' ')[1]
        action.scroll_by_amount(0, 3000).perform()
        browser.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(elem_1)
        browser.find_element(By.TAG_NAME, 'button').click()
        time.sleep(5)

    
    finally:
        browser.quit()