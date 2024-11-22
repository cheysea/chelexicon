from flask import Blueprint

import web_tools.server_lite.modules.statuscodes.controllers
from web_tools.server_lite.modules.statuscodes.controllers.twohundred_controller import TwoHundredController

blueprint= Blueprint('statuscodes', __name__)

@blueprint.route('/200', methods=['GET'])
def statuscodes():
    return TwoHundredController._generate_response()