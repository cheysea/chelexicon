import base64
import json
from time import sleep

import requests
from requests.adapters import HTTPAdapter
from requests.sessions import Session
from urllib3 import Retry


class CreateSession(Session):
    """A class used to create a session object that is preconfigured with a retry strategy and default headers."""

    def __init__(self, url: str = None, params: dict = {}):
        super().__init__()
        self.url: str = url
        self.session:  requests.Session = requests.Session()
        self.set_retry_strategy()
        self.set_headers()
        if params: self.session.params = params

    def __call__(self) -> requests.Session:
        return self.session

    def get(self,
            start_page: int = 1,
            max_page: int = 1,
            retry_sleep = 600,
            **kwargs)-> dict[int: requests.Response]:

            start_page: int = start_page
            max_page: int = max_page
            response_dict: dict = {}

            for page in range(1, max_page+1):
                if page < start_page:
                    continue
                try:
                    retry: bool = True
                    retries: int = 3
                    retried: int = 0
                    while retries >= retried  and retry:
                        self.session.params['page'] = page
                        with self.session:
                            response_dict[page] = super().get(
                                                            url=self.url,
                                                            params=self.session.params,
                                                             **kwargs)

                    if response_dict[page].status_code != 429:
                        retry = False
                    else:
                        retried += 1
                        print(f"Retrying in {retry_sleep} seconds...")
                        sleep(retry_sleep)

                except Exception as e:
                 print(f"Exception: {str(e)}")

            return response_dict

    def is_base64(self, data) -> [str, bool]:
        try:
            result = base64.b64decode(data)
            return result
        except:
            return False

    def is_json(self, data) -> [str, bool]:
        try:
            result = json.loads(data)
            return result
        except:
            return False

    def is_encoded(self, data: str) -> [str, bool]:
        b64decoded_data = self.is_base64(data)
        json_result = self.is_json(b64decoded_data) if b64decoded_data else data
        if json_result:
            response = json_result
        elif b64decoded_data:
            response = b64decoded_data
        else:
            response = False
        return response


    def set_retry_strategy(self,
                           total: int = 5,
                           backoff_factor: float = 0.3,
                           status_forcelist: list = None) -> None:
        """
        Set the retry strategy for the session.
        :param total: The total number of retries.
        :type total: int
        :param backoff_factor:
        :type backoff_factor: float
        :param status_forcelist:
        :type status_forcelist: list
        :return: Nothing returned.
        """
        if status_forcelist is None:
            status_forcelist = [500, 502, 504]
        retry = Retry(
            total = total,
            backoff_factor = backoff_factor,
            status_forcelist = status_forcelist
        )

        self.session.mount('http://', HTTPAdapter(max_retries=retry))
        self.session.mount('https://', HTTPAdapter(max_retries=retry))

    def set_headers(self,
                    headers: dict = {
                        'User-Agent': (
                                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                'AppleWebKit/537.36 '
                                '(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'),
                        'Connection': 'keep-alive',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Referrer': 'https://www.google.com/',
                        'Accept-Encoding': 'gzip',
                        'Accept-Language': 'en-US,en;q=0.9'
                    }
    ):
        """
        Update the session headers with specified values.

        This method updates the headers of a session with the provided dictionary,
        allowing customization of HTTP header fields such as User-Agent, Accept,
        Connection, etc. This is useful for mimicking different browsers or clients
        and for controlling the behavior of the connection.

        :param headers: A dictionary of header field values to update,
                        defaulting to a set of common HTTP headers.
                        The keys are header names and the values are the
                        header values.

        :return: None

        Example usage:

        .. code-block:: python

                Create an instance of the object
                session_object = CreateSession()

                # Set custom headers
                custom_headers = {
                    'User-Agent': 'CustomUserAgent/1.0',
                    'Accept': 'application/json'
                }
                session_manager.set_headers(custom_headers)

                # Access or send requests with updated session headers
                response = session_manager.session.get('https://example.com')
                print(response.status_code)
        """
        self.session.headers.update(headers)


if __name__ == "__main__":
    test_params = {
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
    
    session = CreateSession("https://stfc.pro/api/players", test_params)
    #session = CreateSession("https://www.wikipedia.org")
    response = session.get(max_page=6)
    print(response)
    print("done!")