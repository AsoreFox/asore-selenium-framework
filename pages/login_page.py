from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_locator import LoginLocators

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    
    def load(self, baseUrl):
        self.visit(baseUrl)

    def login(self, username, password):
        self.type(LoginLocators.usernameInput, username)
        self.type(LoginLocators.passwordInput, password)
        self.click(LoginLocators.loginButton)
    
    def get_error_message(self):
        return self.get_text(LoginLocators.errorMessage)
