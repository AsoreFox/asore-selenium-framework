from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

class DeleteAccountLocators(BasePageLocators):
    def __init__(self):
        super().__init__()
    
    account_deleted_title = (By.XPATH, "//*[@data-qa= 'account-deleted']")
    continue_button = (By.XPATH, "//*[@data-qa= 'continue-button']")