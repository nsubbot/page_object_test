from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    # REGISTER_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    # REGISTER_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    # REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")

    # REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
