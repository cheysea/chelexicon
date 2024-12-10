from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from chelexicon.tools.web_tools.server_lite.modules.statuscodes.statuscodes_blueprint import  register_statuscodes_blueprint

        app.register_blueprint(register_statuscodes_blueprint(), url_prefix="/statuscodes")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()