from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_locator import LoginLocators

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def singup(self, name, email):
        expected_title = "New User Signup!"
        result_title = self.get_text(LoginLocators.signup_title)
        assert expected_title == result_title, f"Titulo incorrecto"
        self.type(LoginLocators.signup_name_field, name)
        self.type(LoginLocators.signup_email_field, email)
        self.click(LoginLocators.signup_button)
    
    def get_error_message(self):
        return self.get_text(LoginLocators.errorMessage)
    
