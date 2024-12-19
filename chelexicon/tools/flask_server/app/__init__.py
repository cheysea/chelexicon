"""App module"""

from flask import Flask

from config.config import ConfigureFlask
def create_app():
    """Application factory, used to create and configure application"""
    app = Flask(__name__)
    app.config.from_object("tools.flask_server.app.config.config.DevelopmentConfiguration")

    return app


def configure_app(app):
    """Configurations"""


if __name__ == "__main__":
    app = create_app()
