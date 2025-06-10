from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.account_created_locators import AccountCreatedLocators

class AccountCreatedPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
    
    def verify_account_created_page(self):
        expected_title = "ACCOUNT CREATED!"
        result_title = self.get_text(AccountCreatedLocators.account_created_title)
        assert result_title == expected_title, f"Title is nnot what we expected"
        self.click(AccountCreatedLocators.contiune_button)