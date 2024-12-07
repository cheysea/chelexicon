import logging
import logging.config
log = logging.getLogger(__name__)


class ConfigureFlask():
    TESTING = True

    def configure_flask(self, app):
        app.config.from_object("chelexicon.logging.config.config")

