from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    
    def basket_not_table(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TABLE), 'The basket is not empty'
    
    def basket_null(self):
        text_basket = self.browser.find_element(*BasketPageLocators.BASKET_FALSE_TEXT).text
        assert 'Ваша корзина пуста' in text_basket, 'The basket is not empty'