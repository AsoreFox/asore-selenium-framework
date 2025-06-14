import json
import os
from apis.base_api import BaseApi
from models.user import NewUser
from apis_endpoints.create_account_endpoints import CreateAccountEndpoints

class CreateAccountApi(BaseApi):
    def __init__(self):
        super().__init__()

    def _build_payload(self, user: NewUser):  # Build the payload from the NewUser model, this wont be called from outside. Also converts the NewUser model to a dictionary
        return { 
                "name": user.name,
                "email": user.email,
                "password": user.password,
                "title": user.gender,
                "birth_date": user.days,
                "birth_month": user.months,
                "birth_year": user.years,
                "firstname": user.first_name,
                "lastname": user.last_name,
                "company": user.company,
                "address1": user.address,
                "address2": user.address_2,
                "country": user.country,
                "zipcode": user.zipcode,
                "state": user.state,
                "city": user.city,
                "mobile_number": user.mobile_number,
            }

    def create_account(self, user: NewUser):
        payload = self._build_payload(user)  # Build the payload from the NewUser model
        response = self.post_method(CreateAccountEndpoints.create_account_endpoint(), payload)
        assert response.status_code == 200, f"Response code is not 200 but {response.status_code} and the response is {response.json().get('message')}"
        assert response.json().get("message") == "User created!", f"User creation message mismatch {response.json().get('message')}"
        return response.json()  # Return the JSON response for further processing or assertions
    

