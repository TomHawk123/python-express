from flask import Flask
from .config import Config
from .middleware.security import setup_security
from .database.connections import close_connection
from .middleware import setup_server_middleware
# Import other necessary modules and blueprints


def create_app(config_class=Config):
    app = Flask(__name__)
    setup_server_middleware(app)
    app.config.from_object(config_class)

    app.teardown_appcontext(close_connection)

    # Setup middleware or security features
    setup_security(app)

    # # Register blueprints
    # from .routes import zones, v2
    # app.register_blueprint(zones.bp)
    # app.register_blueprint(v2.bp)

    # You can also initialize other extensions like Flask-Login, Flask-Migrate, etc.

    return app
