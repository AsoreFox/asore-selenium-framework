import json
import os
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

from pages.login_page import LoginPage
from pages.logged_page import LoggedInPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture #loads config file with test data
def config():
    with open(os.path.join("config", "config.json")) as  f:
        return json.load(f)
    homePage = HomePage(driver)
    homePage.visit(config["base_url"])
@pytest.fixture # opnes pages an initialitates the instance of HomePage
def home_page(driver, config):
    home_page = HomePage(driver)
    home_page.visit(config["base_url"])
    return home_page

def test_singup(driver, config, home_page):
    home_page.verify_home_page()
    singup_page = LoginPage(driver)
    name = config["name"]
    email = config["email"]
    singup_page.singup(name, email)