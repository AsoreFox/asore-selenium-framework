import requests

class BaseApi:
    def __init__(self):
        self.base_url = " https://automationexercise.com/api/"


    def get_method(self, api_extension):
        api = self.base_url + api_extension
        response = requests.get(api)
        response.raise_for_status()
        return response.json()
    
    def put_method(self, api_extension, data = None, headers = None, timeout =  10):
        api = self.base_url + api_extension
        response = requests.put(api, json = data, headers= headers, timeout= timeout)
        response.raise_for_status()
        return response.json()
    
    def patch_method(self, api_extension, data =  None, headers =  None, timeout = 10):
        api = self.base_url + api_extension
        response = requests.patch(api, json = data, headers = headers, timeout = timeout)
        response.raise_for_status()
        return response.json()
    
    def post_method(self, api_extension, data =  None, headers =  None, timeout = 10):
        api = self.base_url + api_extension
        response = requests.post(api, json = data, headers = headers, timeout = timeout)
        response.raise_for_status()
        return response.json()
    
    def delete_method(self, api_extension, data =  None, headers =  None, timeout = 10):
        api = self.base_url + api_extension
        response = requests.delete(api, json = data, headers = headers, timeout = timeout)
        response.raise_for_status()
        return response.json()