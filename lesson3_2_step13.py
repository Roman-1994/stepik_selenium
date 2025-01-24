from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def link_reg(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Папа")
            
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Мама")
            
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("Бабушка")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    
    browser.quit()
    
    return welcome_text
    

class TestRegistration(unittest.TestCase):
    
    def test_reg1(self): 
        link = "http://suninjuly.github.io/registration1.html"
        reg_result = link_reg(link)
        self.assertEqual(reg_result, "Congratulations! You have successfully registered!", "ERROR registration")
    
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        reg_result = link_reg(link)
        self.assertEqual(reg_result, "Congratulations! You have successfully registered!", "ERROR registration")

            
if __name__ == "__main__":
    unittest.main()