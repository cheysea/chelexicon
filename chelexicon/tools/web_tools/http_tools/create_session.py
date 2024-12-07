import requests
from requests.adapters import HTTPAdapter
from requests.sessions import Session
from urllib3 import Retry


class CreateSession(Session):
    """A class used to create a session object that is preconfigured with a retry strategy and default headers."""

    def __init__(self, url: str, params: dict):
        super().__init__()
        self.url = url
        self.session:  requests.Session = requests.Session()
        self.set_retry_strategy()
        self.set_headers()
        if params: self.session.params = params

    def __call__(self):
        return self.session

    def get(self, **kwargs):
        return super().get(url=self.url, **kwargs)


    def get_session(self) -> requests.Session:
        """
        Returns the session object.
        :returns: The session object.
        """

        return self.session
        
    def set_retry_strategy(self,
                           total: int = 5,
                           backoff_factor: float = 0.3,
                           status_forcelist: list = None):
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

session = CreateSession("https://stfc.pro/api/players", test_params)
print(session.get())