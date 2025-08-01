from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.delete_account import DeleteAccountPage
import json



class App:
    def __init__(self, driver, config):
        self.home = HomePage(driver)
        self.login = LoginPage(driver)
        self.signup = SignupPage(driver)
        self.created = AccountCreatedPage(driver)
        self.deleted = DeleteAccountPage(driver)
        self.config = config
        self.driver = driver

    def start(self):
        self.home.visit(self.config["base_url"])


