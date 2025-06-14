from apis_endpoints.base_endpoints import BaseEndpoints


class CreateAccountEndpoints(BaseEndpoints):
    def __init__(self):
        if type(self) is CreateAccountEndpoints:
            raise NotImplementedError("This class cannot be instantiated")
        
    __create_account_endpoint = "createAccount"
        
    @staticmethod
    def create_account_endpoint():
        return CreateAccountEndpoints._base_url + CreateAccountEndpoints.__create_account_endpoint
