from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def verify_home_page(self):
        value = self.__getattribute__(HomePageLocators.homePageTitle)
        assert value == "color:orange,", "No te encuentras en la Home Page"
        expectedText = self.get_text(HomePageLocators.homePageText)
        resulText = """AutomationExercise
Full-Fledged practice website for Automation Engineers
All QA engineers can use this website for automation practice and API testing either they are at beginner or advance level. This is for everybody to help them brush up their automation skills."""
    
        assert expectedText == resulText, "El texto de la Home Page es incorrecto"
        image = self.is_visible(HomePageLocators.homePageImage) 
        assert image == True, "La imagen de la Home Page no esta visible"