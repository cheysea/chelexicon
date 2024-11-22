from flask import request, Response

from web_tools.server_lite.modules.statuscodes.controllers.statuscodes_controller import (StatusCodesController)

class TwoHundredController(StatusCodesController,):
    def __init__(self):
        super().__init__()
        super()._generate_response()
        pass

    @staticmethod
    def handle_get_request():
        return Response(status=200)

    @staticmethod
    def handle_post_request():
        pass

    @staticmethod
    def handle_put_request():
        pass

    @staticmethod
    def handle_delete_request():
        pass

