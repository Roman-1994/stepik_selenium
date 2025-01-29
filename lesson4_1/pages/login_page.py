from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, "'login' is not url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTH_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTATION_FORM), "Registration form is not presented"