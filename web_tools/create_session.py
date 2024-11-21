import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class CreateSession():
    """
    CreateSession handles HTTP session creation with retry strategies and custom headers.

    This class provides methods to initialize a session with retry strategies,
    set HTTP headers, and configure session parameters. It employs the "requests"
    library to manage sessions and retry logic for HTTP requests.

    :ivar session: Instance of requests.Session to handle HTTP requests.
    :type session: requests.Session
    """
    def __init__(self):
        self.session:  requests.Session = requests.Session()
        self.set_retry_strategy()
        self.set_headers()

    def get_session(self):
        return self.session
        
    def set_retry_strategy(self,
                           total: int = 5,
                           backoff_factor: float = 0.3,
                           status_forcelist: list = [500, 502, 504]):

        retry = Retry(
            total = total,
            backoff_factor = backoff_factor,
            status_forcelist = status_forcelist
        )

        self.session.mount('http://', HTTPAdapter(max_retries=retry))
        self.session.mount('https://', HTTPAdapter(max_retries=retry))

    def set_headers(self,
                    headers: dict = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
                    }
    ):
        self.session.headers.update(headers)

    def set_parameters(self, parameters: dict):
        self.session.params = parameters