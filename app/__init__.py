from flask import Flask

# Import of Blueprints
from .api.routes import api
from .site.routes import site

# Library to generate log file
from loguru import logger


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(site)

    # Create(if doesn't exist already) a logger directory
    # located in the PATH above
    logger.add("logs/app.log")

    return app
