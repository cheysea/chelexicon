class ConfigureFlask:
    """The class used to configure the flask server."""

    DB_CONNECTION: str = "mongodb+srv://chelsea:aFEu0MkIEVQnceXt@boopit.hq4yw.mongodb.net/?retryWrites=true&w=majority&appName=boopit"
    DEFAULT_DB: str = 'boopit_db'
    CURRENT_DB: str = DEFAULT_DB
    CURRENT_COLLECTION: str = ''
    DB_URI: str = DB_CONNECTION + '/' + CURRENT_DB
    DB_USERNAME: str = 'chelsea'
    DB_PASSWORD: str = 'aFEu0MkIEVQnceXt'
    MONGODB_SETTINGS: dict[str, str] = {
        "db": DEFAULT_DB,
        "host": DB_CONNECTION,
        "username": DB_USERNAME,
        "password": DB_PASSWORD
    }

    STATIC_FOLDER = "/app/static"


class ProductionConfiguration(ConfigureFlask):
    """Configuration class for production environment."""

    DEBUG = False
    TESTING = False


class TestingConfiguration(ConfigureFlask):
    """Configuration class for testing environment."""

    DEBUG = True
    TESTING = True


class DevelopmentConfiguration(ConfigureFlask):
    """Configuration class for development environment."""

    DEBUG = True
    TESTING = True

