from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

class LoginLocators(BasePageLocators):
    def __init__(self):
        super().__init__()

    or_logo = (By.CLASS_NAME, "or")
    singup_title = (By.XPATH, "//*[contains(text(), 'New User Signup!')]")
    singuo_name_field = (By.XPATH, "//*[@data-qa='signup-name']")
    singup_email_field = (By.XPATH, "//*[@data-qa='signup-email']")
    singup_button = (By.XPATH, "//*[@data-qa='signup-button']")
    login_title = (By.XPATH, "//*[contains(text(), 'Login to your account')]")
    login_email_field = (By.XPATH, "//*[@data-qa='login-email']")
    login_password_field = (By.XPATH, "//*[@data-qa='login-password']")
    login_button = (By.XPATH, "//*[@data-qa='login-button']")