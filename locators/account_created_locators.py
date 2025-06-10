from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

class AccountCreatedLocators(BasePageLocators):
    def __init__(self):
        super().__init__()
        
    account_created_title = (By.XPATH, "//*[normalize-space(text()) = 'Account Created!']")
    account_created_text = (By.XPATH, "//*[@class='girl img-responsive']")
    contiune_button = (By.XPATH, "//*[@data-qa= 'continue-button']" )