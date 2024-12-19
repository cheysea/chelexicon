from flask import Blueprint

class ConfigureRoutes:
    """Top-level route configuration class."""

    bp = Blueprint('configure_routes', __name__)

    @bp.route('/')
    def index(self):
        """Route to handle requests to the base url."""
        return 'Hi, friend!'