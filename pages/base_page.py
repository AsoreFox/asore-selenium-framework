from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver, timeout =  10):
        self.driver =  driver 
        self.wait = WebDriverWait(self.driver, timeout)
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
    
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def is_visible(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except:
            return None
    
    def hover_over_scroll_into_wiew(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("""
            const rect = arguments[0].getBoundingClientRect();
            if (rect.top < 0 || rect.bottom > window.innerHeight) {
            arguments[0].scrollIntoView({ behavior: 'auto', block: 'center' });
            }
        """, element)
        ActionChains(self.driver).move_to_element(element).perform()

    def select_from_dropdown(self, locator, value):
        dropdwon = self.is_visible(locator)
        dropdwon.click()
        select = Select(dropdwon)
        select.select_by_value(value)

    def navigate_to_header_menu_option(self , option):
        locator = (By.XPATH, f"//a[contains(text(),'{option}')]")
        element = self.is_visible(locator)
        if not element:
            raise Exception(f"Elmento con xpath:  '{locator}' no esta visible")
        
        style = element.get_attribute("style")
        if "color: orange;" not in style:
            self.click(locator)
            updatedElement = self.is_visible(locator)
            updatedStyle = updatedElement.get_attribute("style")
            assert "color: orange;" in updatedStyle,  f"You are not in the expected page"

        
    def visit(self, url):
        self.driver.get(url)
    
    def verify_user_is_logged_in(self, user_name):
            expected_user = user_name
            result_user = self.get_text(BasePageLocators.user_logged_in_name)
            assert expected_user in result_user, f"Expected {expected_user}, but got {result_user}"
            assert self.is_visible(BasePageLocators.logout_header_button), f"Logout button not visible"
            assert self.is_visible(BasePageLocators.delete_account_header_button), f"Delete account button not visible"
        
    def delete_user(self):
        self.click(BasePageLocators.delete_account_header_button)
    def log_out(self):
        self.click(BasePageLocators.logout_header_button)