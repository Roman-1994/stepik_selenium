from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
    link_11_6 = 'https://omayo.blogspot.com/'
    

    try:
        options = webdriver.ChromeOptions()
        # preferences = {
        #         "download.default_directory" : os.path.join(os.getcwd(), "downloads")
        #         }
        # options.add_experimental_option("prefs", preferences)
        #options.add_argument('--headless=new')
        #options.add_argument('--ignore-certificate-errors')
        #options.add_argument('--ignore-ssl-errors')
        #options.add_argument("--disable-blink-features=AutomationControlled") # Отключение режима автоматизации, чтобы сайт не мог определить, что мы используем WebDriver для автоматизации тестирования
        #options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36") # Изменение браузера на мобильный
        browser = webdriver.Chrome()#options=options)
        browser.maximize_window()
        browser.get(link_11_6)
        #browser.implicitly_wait(10)
        
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
        
        #task_11_6_1
        while True:
            if WebDriverWait(browser, poll_frequency=0.5,timeout=10).until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="DisplayForTimeAndDissapear"]')), message="ERROR_1"):
                break
            else:
                browser.find_element(By.ID, 'sidebar-left-1').send_keys(Keys.END)
                continue
        WebDriverWait(browser, poll_frequency=0.5,timeout=10).until(EC.text_to_be_present_in_element((By.ID, 'deletesuccess'), text_= ''), message="ERROR_1")
        WebDriverWait(browser, poll_frequency=0.5,timeout=10).until(EC.text_to_be_present_in_element((By.ID, 'delayedText'), text_= 'This text is displayed after 10 seconds of wait.'), message="ERROR_2")
        WebDriverWait(browser, poll_frequency=0.5,timeout=10).until(EC.element_to_be_clickable((By.ID, 'timerButton')), message="ERROR_3")
        browser.find_element(By.XPATH, '//button[text()="Try it"]').click()
        WebDriverWait(browser, poll_frequency=0.5,timeout=10).until_not(EC.element_to_be_clickable((By.ID, 'myBtn')), message="ERROR_4")
        
    finally:
        browser.quit()