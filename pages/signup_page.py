from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.signup_locators import SignupLocators
from models.user import NewUser
import datetime

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
        expected_secondary_title = "ADDRESS INFORMATION"
        result_secondary_title = self.get_text(SignupLocators.formulary_second_title)
        assert result_secondary_title.strip() == expected_secondary_title, (
        f"Título incorrecto: se obtuvo '{result_secondary_title}', "
        f"pero se esperaba '{expected_secondary_title}'"
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

    
        self.select_from_dropdown(SignupLocators.days_dropdown, user.days)
        month_number = datetime.datetime.strptime(user.months, '%B').month
        self.select_from_dropdown(SignupLocators.months_dropdown, f"{month_number}")
        self.select_from_dropdown(SignupLocators.years_dropdown, user.years)
        self.select_from_dropdown(SignupLocators.country_dropdown, user.country)

        newsletter_checkbox = user.newsletter
        special_offers_checkbox = user.special_offers
        if newsletter_checkbox:
            self.click(SignupLocators.newsletter_checkbox)
        if special_offers_checkbox:
            self.click(SignupLocators.special_offers_checkbox)

        self.type(SignupLocators.password_field, user.password)
        self.type(SignupLocators.first_name_field, user.first_name)
        self.type(SignupLocators.last_name_field, user.last_name)
        self.type(SignupLocators.company_field, user.company)
        self.type(SignupLocators.address_field, user.address)
        self.type(SignupLocators.secondary_address_field, user.address_2)
        self.type(SignupLocators.state_field, user.state)
        self.type(SignupLocators.city_field, user.city)
        self.type(SignupLocators.zipcode_field, user.zipcode)
        self.type(SignupLocators.mobile_number_field, user.mobile_number)

        self.click(SignupLocators.create_account_button)

        


        


    def get_succes_message(self):
        return self.get_text(SignupLocators.succesMessage)
        
    