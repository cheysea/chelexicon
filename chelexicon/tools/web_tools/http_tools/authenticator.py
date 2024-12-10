import requests

from chelexicon.tools.web_tools.http_tools.create_session import CreateSession


class Authenticator:
    """
    Handles user authentication using basic authentication credentials.

    This class allows setting up basic authentication credentials, performing the
    authentication process with a specified URL, and retrieving the authentication
    cookies which can be used for further requests.

    :ivar session: The session object used for HTTP requests.
    :type session: requests.Session
    :ivar username: The username for basic authentication.
    :type username: str
    :ivar password: The password for basic authentication.
    :type password: str

    Example Usage:

    .. code-block:: python

        import requests
        from your_module import Authenticator

        auth = Authenticator()
        auth.session = requests.Session()

        auth.set_basic_authentication('my_username', 'my_password')
        cookies = auth.authenticate('http://example.com/login')

        print(cookies)
    """

    def __init__(self) -> None:
        self.session: requests.Session = CreateSession().get_session()
        self.username: str = ''
        self.password: str = ''

    def set_basic_authentication(self, username: str, password: str):
        # Set basic authentication to be passed to the URL
        self.username = username
        self.password = password
        
        self.session.auth()
        
    def authenticate(self, url):
        # Connect to the URL passed in by argument and authenticate.
        # Return cookies that should store authentication status.
        session = self.session
        session.get(url)
        return session.cookies
