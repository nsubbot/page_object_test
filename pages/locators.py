from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.CSS_SELECTOR, "a[href*='basket']")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")

    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")

    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div#messages > div:nth-child(3) > div > p > strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")