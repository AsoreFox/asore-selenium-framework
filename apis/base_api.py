import requests
from requests.status_codes import codes

class BaseApi:
    def __init__(self):
        pass    

    def get_method(self, api, timeout = 10):
        response = requests.get(api, timeout=timeout)
        response.raise_for_status()
        return response.json()
    
    def put_method(self, api, data = None, headers = None, timeout =  10):
        response = requests.put(api, json = data, headers= headers, timeout= timeout)
        response.raise_for_status()
        return response.json()
    
    def patch_method(self, api, data =  None, headers =  None, timeout = 10):
        response = requests.patch(api, json = data, headers = headers, timeout = timeout)
        response.raise_for_status()
        return response.json()
    
    def post_method(self, api, data =  None, headers =  None, timeout = 10):
        response = requests.post(api, data = data, headers = headers, timeout = timeout)
        response.raise_for_status()
        return response
    
    def delete_method(self, api, data =  None, headers =  None, timeout = 10):
        response = requests.delete(api, json = data, headers = headers, timeout = timeout)
        response.raise_for_status()
        return response.json()