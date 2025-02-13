from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest

def test_button_start():

    link_6_6_1 = 'https://parsinger.ru/methods/1/index.html'
    link_6_6_2 = 'https://parsinger.ru/selenium/5.5/1/1.html'
    link_6_6_3 = 'https://parsinger.ru/methods/3/index.html'
    link_6_6_4 = 'https://parsinger.ru/selenium/5.5/2/1.html'
    link_6_6_5 = 'https://parsinger.ru/methods/5/index.html'
    link_6_6_7 = 'http://parsinger.ru/scroll/4/index.html'
    link_6_6_8 = 'https://parsinger.ru/selenium/5.5/3/1.html'
    link_6_6_9 = 'https://parsinger.ru/selenium/5.5/4/1.html'
    link_6_6_10 = 'https://parsinger.ru/selenium/5.5/5/1.html'

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        browser = webdriver.Chrome(options=options)
        browser.get(link_6_6_10)
        
        #task_1
        # while True:
        #     result = browser.find_element(By.ID, 'result').text
        #     if result.isdigit():
        #         print(result)
        #         break
        #     else:
        #         browser.refresh()
        
        #task_2
        # elems = browser.find_elements(By.CLASS_NAME, 'text-field')
        # for elem in elems:
        #     elem.clear()
        # browser.find_element(By.ID, 'checkButton').click()
        # alert = browser.switch_to.alert.text
        # print(alert)
        
        #task_3
        # res = 0
        # cookies = browser.get_cookies()
        # for cookie in cookies:
        #     if int(str(cookie['name']).split('_')[-1]) % 2 == 0:
        #         res += int(cookie['value'])
        # print(res)
        
        #task_4
        # elems = browser.find_elements(By.CLASS_NAME, 'text-field')
        # for elem in elems:
        #     if elem.is_enabled():
        #         elem.clear()
        # browser.find_element(By.ID, 'checkButton').click()
        # alert = browser.switch_to.alert.text
        # print(alert)
        
        #task_5
        # link = ''
        # max_expiry = 0
        # elems = browser.find_elements(By.TAG_NAME, 'a')
        # for elem in elems:
        #     #time.sleep(2)
        #     elem.click()
        #     cookies = browser.get_cookies()
        #     for cookie in cookies:
        #         if int(cookie['expiry']) > max_expiry:
        #             max_expiry = int(cookie['expiry'])
        #             link = browser.current_url
        #     browser.back()
        # browser.find_element(By.PARTIAL_LINK_TEXT, link.split('/')[-1].split('.')[0]).click()
        # res = browser.find_element(By.ID, 'result').text
        # print(res)
        
        #task_7
        # res = 0
        # elems = browser.find_elements(By.CLASS_NAME, 'btn')
        # for elem in elems:
        #    browser.execute_script("return arguments[0].scrollIntoView(true);", elem)
        #    elem.click()
        #    res += int(browser.find_element(By.ID, 'result').text)
        # print(res)
        
        #task_8
        # res = 0
        # elems = browser.find_elements(By.CSS_SELECTOR, 'div.parent')
        # for elem in elems:
        #     if elem.find_element(By.CLASS_NAME, 'checkbox').is_selected():
        #         res += int(elem.find_element(By.TAG_NAME, 'textarea').text)
        # print(res)
        
        #task_9
        # elems = browser.find_elements(By.CLASS_NAME, 'parent')
        # for elem in elems:
        #     elem_gray = elem.find_element(By.CSS_SELECTOR, '[color="gray"]').text
        #     elem.find_element(By.CSS_SELECTOR, '[color="gray"]').clear()
        #     elem.find_element(By.CSS_SELECTOR, '[color="blue"]').send_keys(elem_gray)
        #     elem.find_element(By.TAG_NAME, 'button').click()
        #     assert elem.find_element(By.CSS_SELECTOR, '[color="gray"]').get_attribute('style') == 'background-color: green;', 'ERROR'
        # browser.find_element(By.ID, 'checkAll').click()
        # print(browser.find_element(By.ID, 'congrats').text)
        
        #task_10
        parent_div = browser.find_element(By.ID, 'main-container')
        child_divs = parent_div.find_elements(By.XPATH, './div')
        for div in child_divs:
            color = div.find_element(By.TAG_NAME, 'span').text
            select = Select(div.find_element(By.TAG_NAME, 'select'))
            select.select_by_value(color)
            div.find_element(By.CSS_SELECTOR, f'[data-hex="{color}"]').click()
            div.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
            div.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys(color)
            button = div.find_element(By.XPATH, './button[text()="Проверить"]')
            button.click()
            assert button.text == 'ОК', 'ERROR'
        browser.find_element(By.XPATH, '//button[text()="Проверить все элементы"]').click()
        print(browser.switch_to.alert.text)

    
    finally:
        browser.quit()