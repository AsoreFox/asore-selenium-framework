import json
import os
import pytest
from pages.login_page import LoginPage
from pages.logged_page import LoggedInPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def config():
    with open(os.path.join("config", "config.json")) as  f:
        return json.load(f)

def test_login_success(driver, config):
    loginPage = LoginPage(driver)
    loginPage.load(config["base_url"])
    loginPage.login(config["username"], config["password"])
    loggedInPage = LoggedInPage(driver)
    succesText = loggedInPage.get_succes_message()

    assert succesText == "Logged In Successfully"

def test_login_incorrect_user(driver, config):
    loginPage = LoginPage(driver)
    loginPage.load(config["base_url"])
    loginPage.login("Carlos", config["password"])
    errorMessage = loginPage.get_error_message()

    assert errorMessage == "Your username is invalid!"

def test_login_incorrect_password(driver, config):
    loginPage = LoginPage(driver)
    loginPage.load(config["base_url"])
    loginPage.login(config["username"], "Saminawakawakaeee")
    errorMessage = loginPage.get_error_message()

    assert errorMessage == "Your password is invalid!"
