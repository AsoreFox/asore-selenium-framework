class BaseEndpoints:
    def __init__(self):
        if type(self) is BaseEndpoints:
            raise NotImplementedError("This class cannot be instantiated")
    _base_url = "https://automationexercise.com/api/"