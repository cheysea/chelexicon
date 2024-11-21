import requests

#from chelseas_cookbook.web_tools import CreateSession
import chelseas_cookbook

class Authenticator:
    # This class is used to authenticate to websites using Sessions
    # from the python 'requests' library

    def __init__(self) -> None:
        self.session: Session = None
        self.username: str = ''
        self.password: str = ''
        
        return

    def set_basic_authentication(self, username: str, password: str):
        self.username = username
        self.password = password
        
        session.auth()
        
    def authenticate():
        session = self.session
        session.get('https://www.google.com')
