from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

class HomePageLocators(BasePageLocators):
    homePageText = (By.XPATH, "//*[@class = 'col-sm-6'][1]")
    homePageImage = (By.XPATH, "//*[@class='girl img-responsive']")