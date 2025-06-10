from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.signup_locators import SignupLocators
from models.user import NewUser

class SignupPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    
    def verify_signup_page(self, user: NewUser):
        expected_title = "ENTER ACCOUNT INFORMATION"
        result_title = self.get_text(SignupLocators.formulary_title)
        assert result_title.strip() == expected_title, (
        f"Título incorrecto: se obtuvo '{result_title}', "
        f"pero se esperaba '{expected_title}'"
        )
        expected_name = user.name
        result_name = self.is_visible(SignupLocators.name_field)
        assert result_name.get_attribute("value") in expected_name, f"Name is not what we inputed in the pevious page {user.name}"
        expected_email = user.email
        result_email = self.is_visible(SignupLocators.email_field)
        assert result_email.get_attribute("value") in expected_email, f"Email is not what we inputed in the previous page"
        assert not result_email.is_enabled(), f"Field is not disabled"

    def fill_formulary(self, user: NewUser):
        if user.gender != "Mr.":
            gender_checkbox = SignupLocators.gender_checbox_1
        else:
            gender_checkbox = SignupLocators.gender_checbox_2
        self.click(gender_checkbox)


        


    def get_succes_message(self):
        return self.get_text(SignupLocators.succesMessage)
        
    