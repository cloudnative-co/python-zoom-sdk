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
    def get(self, userId: str, login_type: str = None):
        query = get_arguments(locals())
        path = "{}/{}".format(self.path, userId)
        del query["userId"]
        response = self.request(method="get", path=path, query = query)
        return response

    @validation
    def update(
        self, userId: str, login_type: str = None, first_name: str = None,
        last_name: str = None, type: int = None, pmi: int = None,
        use_pmi: bool = None, timezone: str = None, language: str = None,
        dept: str = None, vanity_name: str = None, host_key: str = None,
        cms_user_id: str = None, job_title: str = None, company: str = None,
        location: str = None, phone_number: str = None,
        phone_country: str = None
    ):
        args = locals()
        path = "{}/{}".format(self.path, userId)
        query = get_arguments(args, ["login_type"])
        payload = get_arguments(args=args, ignores=["login_type", "userId"])
        response = self.request(
            method="patch", path=path, query = query, payload=payload
        )
        return response

    @validation
    def meetings(self, userId: str, type: str = None, page_size: int = 30, page_number: int = 1):
        query = get_arguments(locals())
        path = "{}/{}/meetings".format(self.path, userId)
        del query["userId"]
        response = self.request(method="get", path=path, query = query)
        return response

