import json
import os
import pytest
from models.user import NewUser

@pytest.fixture #loads config file with test data
def config():
    with open(os.path.join("config", "config.json")) as  f:
        return json.load(f)
    

@pytest.fixture
def user():
    with open(os.path.join("config", "user.json")) as  f:
        return json.load(f)
    


def test_singup(config, app, user):
    user = NewUser(**{k: user[k] for k in NewUser.__annotations__}) #instancia el usuario desde el json
    app.home.verify_home_page()
    app.home.navigate_to_header_menu_option("Signup / Login")
    name = config["name"]
    email = config["email"]
    app.login.singup(name, email)
    app.signup.verify_signup_page(user)
    app.signup.fill_formulary(user)
    app.created.verify_account_created_page()
    app.home.verify_user_is_logged_in(user.name)
    app.home.delete_user()
    app.deleted.verify_account_is_deleted()





