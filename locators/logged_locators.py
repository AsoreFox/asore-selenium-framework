from selenium.webdriver.common.by import By
from locators.home_page_locators import HomePageLocators

class LoggedLocators(HomePageLocators):
    succesMessage= (By.CLASS_NAME, "post-title")