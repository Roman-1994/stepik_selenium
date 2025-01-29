from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTATION_FORM = (By.CSS_SELECTOR, "#register_form")
    AUTH_FORM = (By.ID, "login_form")

class MainPageLinks():
    LINK_1 = "http://selenium1py.pythonanywhere.com/"
    LINK_2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    LINK_3 = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"