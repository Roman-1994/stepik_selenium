from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTATION_FORM = (By.CSS_SELECTOR, "#register_form")
    AUTH_FORM = (By.ID, "login_form")
    INPUT_EMAIL = (By.ID, "id_registration-email")
    INPUT_PASS_1 = (By.ID, "id_registration-password1")
    INPUT_PASS_2 = (By.ID, "id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")
    
class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class MainPageLinks():
    LINK_1 = "http://selenium1py.pythonanywhere.com/"
    LINK_2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    LINK_3 = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    
class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_TABLE = (By.CSS_SELECTOR, ".basket-title")
    BASKET_FALSE_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    