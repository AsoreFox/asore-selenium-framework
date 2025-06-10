from selenium.webdriver.common.by import By
from locators.home_page_locators import HomePageLocators

class SignupLocators(HomePageLocators):
    def __init__(self):
        super().__init__()



        
    formulary_title = (By.XPATH, "//*[normalize-space(text()) = 'Enter Account Information']")
    gender_checbox_1 = (By.ID, "id_gender1")
    gender_checbox_2 = (By.ID, "id_gender2")
    name_field = (By.ID, "name")
    email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    days_dropdown = (By.ID, "days")
    months_dropdown = (By.ID, "months")
    years_dropdown = (By.ID, "years")
    newsletter_checkbox = (By.ID, "newsletter")
    special_offers_checkbox = (By.ID, "optin")
    first_name_field = (By.ID, "first_name")
    last_name_field = (By.ID, "last_name")
    company_fiel = (By.ID, "company")
    address_field = (By.ID, "address1")
    secondary_address_field = (By.ID, "address2")
    countr_dropdown = (By.ID, "country")
    stat_field = (By.ID, "state")
    city_field =  (By.ID, "city")
    zipcode_field = (By.ID, "zipcode")
    mobile_numer_field = (By.ID, "mobile_number")