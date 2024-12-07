from abc import ABC, abstractmethod
from flask import request


class StatusCodesController(ABC):
    def send_response(self):
        #if request.method == 'GET':
        return self.handle_get_request()

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