from selenium.webdriver.common.by import By
import time

class TestLanguage:
    def test_language_user(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        browser.implicitly_wait(20)
        
        time.sleep(30)
        
        button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
        
        assert button, 'NOT BUTTON'