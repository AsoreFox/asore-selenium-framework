import requests

class LoginApi:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def login(self, usuername, password):
        endpoint = f"{self.base_url}/login"
        payload = {
            "username": usuername,
            "password": password
        }
        response = requests.post(endpoint, json = payload)
        return response
