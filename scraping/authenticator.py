import requests

class Authenticator:
    # This class is used to authenticate to websites using Sessions
    # from the python 'requests' library

    def __init__(self) -> None:
        self.username: str = ''
        self.password: str = ''
        return

    def set_authentication(self, username: str, password: str):
        self.username = username
        self.password = password