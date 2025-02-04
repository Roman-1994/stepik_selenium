from .pages.product_page import ProductPage
import pytest

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link2)
    page.open()
    page.add_product_in_basket()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link2)
    page.open()
    page.should_not_be_success_message()
    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link2)
    page.open()
    page.add_product_in_basket()
    page.should_not_be_success_message_disappeared()