import json
import os
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.delete_account import DeleteAccountPage
from models.user import NewUser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture #loads config file with test data
def config():
    with open(os.path.join("config", "config.json")) as  f:
        return json.load(f)
    homePage = HomePage(driver)
    homePage.visit(config["base_url"])

@pytest.fixture
def user():
    with open(os.path.join("config", "user.json")) as  f:
        return json.load(f)
    
@pytest.fixture # opnes pages an initialitates the instance of HomePage
def home_page(driver, config):
    home_page = HomePage(driver)
    home_page.visit(config["base_url"])
    return home_page

def test_singup(driver, config, home_page, user):
    user = NewUser(**{k: user[k] for k in NewUser.__annotations__}) #instancia el usuario desde el json
    home_page.verify_home_page()
    home_page.navigate_to_header_menu_option("Signup / Login")
    name = config["name"]
    email = config["email"]
    login_page = LoginPage(driver)
    login_page.singup(name, email)
    signup_page = SignupPage(driver)
    signup_page.verify_signup_page(user)
    signup_page.fill_formulary(user)
    account_created_page = AccountCreatedPage(driver)
    account_created_page.verify_account_created_page()
    home_page.verify_user_is_logged_in(user.name)
    home_page.delete_user()
    deleted_account_page = DeleteAccountPage(driver)
    deleted_account_page.verify_account_is_deleted()


