import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class CreateSession:
    def __init__(self):
        self.session:  requests.Session = requests.Session()
        self.set_retry_strategy()
        self.set_headers()

    def get_session(self):
        return self.session
        
    def set_retry_strategy(self,
                           total: int = 5,
                           backoff_factor: float = 0.3,
                           status_forcelist: list = None):
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
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9'
                    }
    ):
        self.session.headers.update(headers)

    def set_parameters(self, parameters: dict):
        self.session.params = parameters