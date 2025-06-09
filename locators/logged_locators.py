from selenium.webdriver.common.by import By
from locators.home_page_locators import HomePageLocators

class LoggedLocators(HomePageLocators):
    def __init__(self):
        super().__init__()
        
    succesMessage = (By.CLASS_NAME, "post-title")