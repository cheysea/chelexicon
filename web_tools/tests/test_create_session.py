# File: test_create_session.py

import pytest
import requests
from web_tools.create_session import CreateSession
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from wiremock.server import WireMockServer
from wiremock.resources.mappings import Mapping, MappingRequest, MappingResponse
from wiremock.client import ClientException


@pytest.fixture
def create_session_instance():
    """
    Fixture to provide an instance of CreateSession for use in the tests.
    """
    return CreateSession()


@pytest.fixture(scope="module")
def wiremock_server():
    """
    Fixture to set up and tear down a WireMock server.
    """
    server = WireMockServer(port=8080)
    server.start()
    yield server
    server.stop()


def test_session_initialization(create_session_instance):
    """
    Test the initialization of the session object.

    The test ensures that the session object is properly created and is an 
    instance of requests.Session.
    """
    assert isinstance(create_session_instance.session,
                      requests.Session), "Session should be an instance of requests.Session"


def test_get_session(create_session_instance):
    """
    Test the get_session method.

    The test ensures that get_session method returns the session object.
    """
    session = create_session_instance.get_session()
    assert session is create_session_instance.session, "get_session should return the session object"


def test_set_retry_strategy_default(create_session_instance):
    """
    Test the default retry strategy settings.

    The test ensures that the default retry strategy is applied correctly.
    """
    adapter = create_session_instance.session.get_adapter('http://')
    assert isinstance(adapter, HTTPAdapter), "Adapter should be an instance of HTTPAdapter"
    assert adapter.max_retries.total == 5, "Default total retries should be 5"
    assert adapter.max_retries.backoff_factor == 0.3, "Default backoff_factor should be 0.3"
    assert adapter.max_retries.status_forcelist == [500, 502, 504], "Default status_forcelist should be [500, 502, 504]"


def test_set_retry_strategy_custom(create_session_instance):
    """
    Test custom retry strategy settings.

    The test ensures that the custom retry strategy can be applied correctly.
    """
    create_session_instance.set_retry_strategy(total=3, backoff_factor=1, status_forcelist=[400, 403])
    adapter = create_session_instance.session.get_adapter('http://')
    assert adapter.max_retries.total == 3, "Custom total retries should be 3"
    assert adapter.max_retries.backoff_factor == 1, "Custom backoff factor should be 1"
    assert adapter.max_retries.status_forcelist == [400, 403], "Custom status forcelist should be [400, 403]"




def test_set_headers_default(create_session_instance):
    """
    Test the default headers.

    The test ensures that default headers are set correctly.
    """
    headers = create_session_instance.session.headers
    assert headers[
               'User-Agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', "Default User-Agent header should be set"


def test_set_headers_custom(create_session_instance):
    """
    Test setting custom headers.

    The test ensures that custom headers can be added correctly.
    """
    custom_headers = {'Authorization': 'Bearer <token>'}
    create_session_instance.set_headers(custom_headers)
    headers = create_session_instance.session.headers
    assert headers['Authorization'] == 'Bearer <token>', "Custom Authorization header should be set"


def test_set_parameters(create_session_instance):
    """
    Test the set_parameters method.

    The test ensures that the parameters can be set correctly in the session.
    """
    params = {'key1': 'value1', 'key2': 'value2'}
    create_session_instance.set_parameters(params)
    assert create_session_instance.session.params == params, "Session parameters should be set correctly"
