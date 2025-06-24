from apis.base_api import BaseApi
from apis_endpoints.delete_user_account_endpoints import DeleteUserAccountEndpoints
from models.user import NewUser  # Assuming User model is defined in models.user

class DeleteUserAccountApi(BaseApi):
    def __init__(self):
        super().__init__()

    def _build_payload(self, user: NewUser):
        return {
            "email": user.email,
            "password": user.password
        }

    def delete_account(self, user: NewUser):
        payload = self._build_payload(user)
        response = self.delete_method(DeleteUserAccountEndpoints.delete_account_endpoint(), payload)
        assert response.status_code == 200, f"Response code is not 200 but {response.status_code} and the response is {response.json().get('message')}"
        assert response.json().get("message") == "Account deleted!", f"User deletion message mismatch {response.json().get('message')}"
        return response.json()  # Return the JSON response for further processing or assertions