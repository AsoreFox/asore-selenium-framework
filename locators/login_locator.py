from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

class LoginLocators(BasePageLocators):
    def __init__(self):
        super().__init__()

    or_logo = (By.CLASS_NAME, "or")
    signup_title = (By.XPATH, "//*[contains(text(), 'New User Signup!')]")
    signup_name_field = (By.XPATH, "//*[@data-qa='signup-name']")
    signup_email_field = (By.XPATH, "//*[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//*[@data-qa='signup-button']")
    login_title = (By.XPATH, "//*[contains(text(), 'Login to your account')]")
    login_email_field = (By.XPATH, "//*[@data-qa='login-email']")
    login_password_field = (By.XPATH, "//*[@data-qa='login-password']")
    login_button = (By.XPATH, "//*[@data-qa='login-button']")