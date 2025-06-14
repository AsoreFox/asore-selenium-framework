from apis_endpoints.base_endpoints import BaseEndpoints


class LoginEndpoints(BaseEndpoints):
    def __init__(self):
        if type(self) is LoginEndpoints:
            raise NotImplementedError("This class cannot be instantiated")
    
    __login_endpoint = "login"
    
    @staticmethod
    def login_endpoint():
        return LoginEndpoints._base_url + LoginEndpoints.__login_endpoint