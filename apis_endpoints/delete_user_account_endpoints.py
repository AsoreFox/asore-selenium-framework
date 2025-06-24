from apis_endpoints.base_endpoints import BaseEndpoints


class DeleteUserAccountEndpoints(BaseEndpoints):
    def __init__(self):
        super().__init__()
        if type(self) is DeleteUserAccountEndpoints:
            raise NotImplementedError("This class cannot be instantiated")
        

    __delete_account_endpoint = "deleteAccount"


    @staticmethod
    def delete_account_endpoint():
        return DeleteUserAccountEndpoints._base_url + DeleteUserAccountEndpoints.__delete_account_endpoint
