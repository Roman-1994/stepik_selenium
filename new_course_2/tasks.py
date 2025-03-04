from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

def test_button_start():

    link_4_6_1 = 'https://vk.com/'
    link_4_6_2 = 'https://stepik.org/catalog'
    link_6_3 = 'https://testautomationpractice.blogspot.com/'
    link_7_8 = 'https://hyperskill.org/tracks'
    link_8_6_1 = 'https://demoqa.com/text-box'
    link_8_6_2 = 'http://the-internet.herokuapp.com/status_codes'
    link_10_5_1 = 'https://demoqa.com/upload-download'
    

    try:
        options = webdriver.ChromeOptions()
        # preferences = {
        #         "download.default_directory" : os.path.join(os.getcwd(), "downloads")
        #         }
        # options.add_experimental_option("prefs", preferences)
        #options.add_argument('--headless=new')
        #options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome()#options=options)
        browser.maximize_window()
        browser.get(link_10_5_1)
        browser.implicitly_wait(10)
        
        #task_4_6
        # title_1 = browser.title
        # print(title_1)
        # browser.get(link_4_6_2)
        # title_2 = browser.title
        # print(title_2)
        # browser.back()
        # assert browser.title == title_1, 'Не удалось вернуться на предыдущую страницу'
        # browser.refresh()
        # url_1 = browser.current_url
        # print(url_1)
        # browser.get(link_4_6_2)
        # assert url_1 != browser.current_url, 'Не удалось перейти на следующую страницу'
        
        #task_6_3
        # assert browser.find_element(By.CLASS_NAME, 'wikipedia-icon'), 'ERROR_1'
        # assert browser.find_element(By.ID, 'Wikipedia1_wikipedia-search-input'), 'ERROR_2'
        # assert browser.find_element(By.CLASS_NAME, 'wikipedia-search-button'), 'ERROR_3'
        
        #task_7_8
        # assert browser.find_element(By.XPATH, "//div[contains(@class, 'flex')]/a[text()='Python']"), 'ERROR_1'
        # assert browser.find_element(By.XPATH, "((//div[contains(@class, 'flex flex-wrap items-center gap-3')])[2]/span)[1]/*[name()='svg']/*[name()='path']"), 'ERROR_2'
        
        #task_8_6_1
        # elems_input = browser.find_elements(By.TAG_NAME, 'input')
        # elems_textarea = browser.find_elements(By.TAG_NAME, 'textarea')
        # output = 'test'
        # for elem in elems_input:
        #     elem.clear()
        #     elem.send_keys(output)
        #     assert elem.get_attribute('value') == output, 'ERROR'
        # for elem in elems_textarea:
        #     elem.clear()
        #     elem.send_keys(output)
        #     assert elem.get_attribute('value') == output, 'ERROR'
        
        #task_8_6_2
        # elems = browser.find_elements(By.XPATH, '(//ul//a)')
        # for elem in elems:
        #     elem.click()
        #     time.sleep(1)
        #     browser.back()
        #     time.sleep(1)
        
        #task_10_5_1
        # elem = browser.find_element(By.ID, 'uploadFile')
        # elem.send_keys(os.path.join(os.getcwd(), "1.png"))
        
        
                        
        
    finally:
        browser.quit()