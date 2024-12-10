from flask import request, Response

from chelexicon.tools.web_tools.server_lite.modules.statuscodes.controllers.statuscodes_controller import (StatusCodesController)

class TwoHundredController(StatusCodesController,):
    def __init__(self):
        super().__init__()

    def send_response(self):
        super().send_response()

    def handle_get_request(self):
        return print("Yay! You made it!")

    @staticmethod
    def handle_post_request():
        pass

    @staticmethod
    def handle_put_request():
        pass

    @staticmethod
    def handle_delete_request():
        pass

