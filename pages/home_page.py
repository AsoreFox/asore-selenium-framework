from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def verify_home_page(self):
        self.navigate_to_header_menu_option("Home")
        result_text = self.get_text(HomePageLocators.home_page_text)
        expected_text = """AutomationExercise
Full-Fledged practice website for Automation Engineers
All QA engineers can use this website for automation practice and API testing either they are at beginner or advance level. This is for everybody to help them brush up their automation skills.
Test Cases APIs list for practice"""
    
        assert result_text == expected_text, f"Text is different from expected"
        image = self.is_visible(HomePageLocators.home_page_image) 
        assert image , f"La imagen de la Home Page no esta visible"