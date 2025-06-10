from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.delete_account_locators import DeleteAccountLocators

class DeleteAccountPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def verify_account_is_deleted(self):
        expected_title = "ACCOUNT DELETED!"
        result_title = self.get_text(DeleteAccountLocators.account_deleted_title)
        assert result_title == expected_title, f"Title is nnot what we expected"