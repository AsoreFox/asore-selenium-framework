import pytest
import json
import os
from apis.login import LoginApi
from models.user import NewUser
from apis.create_account import CreateAccountApi
from apis.delete_user_account import DeleteUserAccountApi

BASE_URL = "https://your-api-url.com"

@pytest.fixture #loads config file with test data
def config():
    with open(os.path.join("config", "config.json")) as  f:
        return json.load(f)

@pytest.fixture
def user():
    with open(os.path.join("config", "user.json")) as  f:
        return json.load(f)
    
@pytest.fixture
def api():
    return CreateAccountApi() 

def test_create_account(api_handler, user):
    user = NewUser(**{k: user[k] for k in NewUser.__annotations__}) #instancia el usuario desde el json
    api_handler.create.create_account(user)
    api_handler.delete.delete_account(user)
    