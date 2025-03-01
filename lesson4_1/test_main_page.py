from .pages.main_page import MainPage
from .pages.locators import MainPageLinks
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    #@pytest.mark.skip
    def test_guest_can_go_to_login_page(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/"
        #page = MainPage(browser, link)
        page = MainPage(browser, MainPageLinks.LINK_1)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    #@pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/"
        #page = MainPage(browser, link)
        page = MainPage(browser, MainPageLinks.LINK_1)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.window_handles)
    page.basket_not_table()
    page.basket_null()
    
