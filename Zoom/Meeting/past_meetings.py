# -*- coding:utf-8 -*-
__author__ = "Sebastian  <seba@cloudnative.co.jp>"
__status__ = "production"
__version__ = "1.0.0"
__date__    = "2020-02-20"
from ..client import Client
from ..Utils import validation, get_arguments


class PastMeetings(Client):
    """
    @namespace  Zoom.Meetings.PastMeetings
    @class      PastMeetings
    """
    path = "/past_meetings/{meetingId}"

    @validation
    def instances(self, meetingId: int):
        """
        @brief          Get a list of ended meeting instances
        @params[in]     meetingId(int)
        @n              The meeting ID.
        """
        query = get_arguments(locals())
        path = self.path.format(**query) + "/instances"
        return self.request(method="get", path=path)

    @validation
    def participants(
        self, meetingId: int, page_size: int = 0,
        next_page_token: str = None
    ):
        """
        @brief          Get a list of ended meeting instances
        @params[in]     meetingId(int)
        @n              The meeting ID.
        @params[in]     page_size(int)
        @n              The number of records returned within a single API call
        @params[in]     next_page_token(str)
        @n              The next page token is used to paginate
        @n              through large result sets. A next page token will be
        @n              returned whenever the set of available results exceeds
        @n              the current page size. The expiration period for this
        @n              token is 15 minutes.
        """
        query = get_arguments(locals())
        path = self.path.format(**query) + "/participants"
        del query["meetingId"]
        return self.request(method="get", path=path, query=query)

    @validation
    def details(self, meetingId: int):
        """
        @brief          Get details on a past meeting.
        @params[in]     meetingId(int)
        @n              The meeting ID.
        """
        query = get_arguments(locals())
        path = self.path.format(**query)
        return self.request(method="get", path=path)
