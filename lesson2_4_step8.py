from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    if WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100')):
        button_1 = browser.find_element(By.ID, 'book')
        button_1.click()
    
        x = int(browser.find_element(By.ID, "input_value").text)
        y = calc(x)
        
        inp = browser.find_element(By.ID, "answer")
        inp.send_keys(y)
        
        button_2 = browser.find_element(By.ID, 'solve')
        button_2.click()

finally:
    time.sleep(10)
    browser.quit()