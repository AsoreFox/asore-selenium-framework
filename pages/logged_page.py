from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.logged_locators import LoggedLocators

class LoggedInPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def get_succes_message(self):
        return self.get_text(LoggedLocators.succesMessage)
        
    