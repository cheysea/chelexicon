from flask import Blueprint


from chelexicon.tools.web_tools.server_lite.modules.statuscodes.controllers.twohundred_controller import TwoHundredController

def register_statuscodes_blueprint():
    blueprint= Blueprint('statuscodes', __name__)

    @blueprint.route('/200', methods=['GET'])
    def statuscodes():
        obj = TwoHundredController()
        return obj.send_response()

    return blueprint

