import requests
import json
from retrying import retry

from chelexicon.tools.web_tools.http_tools.create_session import CreateSession

test_params =  {
        "type": "player_data_power",
        "page": 1,
        "pageCount": 250,
        "region": "",
        "server": 92,
        "level": "",
        "sortBy": "rank",
        "sortOrder": "asc",
        "search": "",
        "searchMatch": "false",
        "tag": "",
        "rankMatch": "false"
    }


class CallUrl:
    def __init__(self, url: str, params: dict = {}):
        if params: self.session.params = params
        self.session = CreateSession().get_session()
        self.url = url

    # TODO: Add a method to make the call. Or should this just be handled by
    # the requests library?
    # TODO: Build the Retry Pattern

    def call_url(self):
        response = self.session.get(self.url)
        return response

    def get


print(CallUrl("https://stfc.pro/api/players", test_params).call_url())