from ..client import Client
from ..Utils import validation
from ..Utils import get_arguments


class Meetings(Client):
    """
    @namespace  Jamf.Computer
    @class      Meetings
    @brief      コンピューター操作用クラス
    """
    path = "/meetings/{meetingId}"

    @validation
    def get(self, meetingId: int, occurrence_id: str = None):
        query = get_arguments(locals())
        path = self.path.format(**query)
        del query["meetingId"]
        return self.request(method="get", path=path, query=query)
