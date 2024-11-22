from abc import ABC, abstractmethod
from flask import request


class StatusCodesController(ABC):
    def __init__(self):
        pass

    def _generate_response(self):
        #if request.method == 'GET':
        self.handle_get_request()

    @abstractmethod
    def handle_get_request(self):
        pass

    @staticmethod
    @abstractmethod
    def handle_post_request(self):
        pass

    @staticmethod
    @abstractmethod
    def handle_put_request(self):
        pass

    @staticmethod
    @abstractmethod
    def handle_delete_request(self):
        pass