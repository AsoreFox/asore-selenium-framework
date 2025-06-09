from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

class HomePageLocators(BasePageLocators):
    home_page_text = (By.XPATH, "//*[@class = 'col-sm-6'][1]")
    home_page_image = (By.XPATH, "//*[@class='girl img-responsive']")