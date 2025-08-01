from apis.create_account import CreateAccountApi
from apis.login import LoginApi
from apis.delete_user_account import DeleteUserAccountApi
from apis.base_api import BaseApi

class ApiHandler:
    def __init__(self):
        self.base_api = BaseApi()
        self.create = CreateAccountApi()
        self.login = LoginApi()
        self.delete = DeleteUserAccountApi()

