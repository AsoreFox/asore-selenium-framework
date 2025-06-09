from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_locator import LoginLocators

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def singup(self, name, email):
        self.navigate_to_header_menu_option(LoginLocators.login_singup_page_header_button)
        expected_title = "New User Signup!"
        result_title = self.get_text(LoginLocators.singup_title)
        assert expected_title == result_title, f"Titulo incorrecto"
        self.type(LoginLocators.singuo_name_field, name)
        self.type(LoginLocators.singup_email_field, email)
        self.click(LoginLocators.singup_button)
    
    def get_error_message(self):
        return self.get_text(LoginLocators.errorMessage)
