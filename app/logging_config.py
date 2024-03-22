import logging
from flask.logging import default_handler


def setup_logging(app):
    app.logger.removeHandler(default_handler)
    logging.basicConfig(level=logging.INFO)  # Or DEBUG, ERROR, etc.
