from apis.base_api import BaseApi
from apis_endpoints.login_endpoints import LoginEndpoints # Assuming you have a LoginEndpoints class similar to CreateAccountEndpoints

class LoginApi(BaseApi):
    def __init__(self):
        super().__init__()

    def _build_payload(self, username, password):
        return {
            "username": username,
            "password": password
        }

    def login(self, username, password):
        payload = self._build_payload(username, password)
        response = self.post_method(LoginEndpoints.login_endpoint(), payload)
        assert response.status_code == 200, f"Response code is not 200 but {response.status_code} and the response is {response.json().get('message')}"
        assert response.json().get("message") == "Login successful", f"Login message mismatch {response.json().get('message')}"
        return response
