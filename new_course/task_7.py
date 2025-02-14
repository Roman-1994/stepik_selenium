from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest

def test_button_start():

    link_7_1_6 = 'https://parsinger.ru/selenium/7/7.1/index.html'
    link_7_2_5 = 'https://parsinger.ru/selenium/7/7.2/index.html'
    

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        browser = webdriver.Chrome(options=options)
        browser.get(link_7_2_5)
        browser.implicitly_wait(3)
        
        #task_7_1_6
        # height_body = browser.execute_script("return document.body.scrollHeight")
        # browser.execute_script(f'window.scrollTo(0, {height_body});')
        # time.sleep(3)
        # print(browser.find_element(By.ID, 'secret-container').text)
        
        #task_7_2_5
        #elems = browser.find_element(By.CLASS_NAME, 'interactive')
        for i in range(1, 101):
            elems = browser.find_element(By.CSS_SELECTOR, f'div.input-container div.input-wrapper:nth-child({i}) .interactive')
            elems.send_keys('1')
            elems.send_keys(Keys.ENTER)
            elems.send_keys(Keys.ARROW_DOWN)
            browser.execute_script("return arguments[0].scrollIntoView(true);", elems)
            time.sleep(1)
        print(browser.find_element(By.ID, 'hidden-password').text)

    
    finally:
        browser.quit()