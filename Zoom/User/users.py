from ..client import Client
from ..Utils import validation
from ..Utils import get_arguments

class Users(Client):
    """
    @namespace  Zoom.Users
    @class      Meetings
    """
    path = "/users"

    @validation
    def list(self, status: str = None, page_size: int = None, page_number: int = None, role_id: str = None):
        query = get_arguments(locals())
        response = self.request(method="get", path=self.path, query=query)
        return response

    @validation
    def meetings(self, userId: str, type: str = None, page_size: int = 30, page_number: int = 1):
        query = get_arguments(locals())
        path = "{}/{}/meetings".format(self.path, userId)
        del query["userId"]
        response = self.request(method="get", path=path, query = query)
        return response
