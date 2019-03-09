import logging
from app import create_app

APP = create_app()
GUNICORN_LOGGER = logging.getLogger('gunicorn.error')
APP.logger.handlers = GUNICORN_LOGGER.handlers
