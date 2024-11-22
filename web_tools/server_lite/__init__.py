from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from web_tools.server_lite.modules.statuscodes import statuscodes_blueprint

        app.register_blueprint(statuscodes_blueprint.blueprint, url_prefix="/statuscodes")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()