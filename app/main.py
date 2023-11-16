# -*- coding: utf-8 -*-
import os

from flask import Flask

import config
from app.extensions import db
from app.extensions import v1_api


def create_app(name=None, env=None):
    """Create the Flask app instance that used throughout the application.

    Args:
        name: The name of the Flask application package.
        env: An environment variable to specify the environment in which
        the Flask application is running such as development, production,
        testing.
    Returns:
        Application object (instance of flask.Flask)
    """
    app = Flask(name or __name__)

    # Load default settings and from environment
    app.config.from_pyfile(config.DEFAULT_CONFIG_PATH)
    env = (env or os.getenv('FLASK_ENVIRONMENT', 'development')).upper()
    if env == 'TEST':
        app.config.from_pyfile(config.TEST_CONFIG_PATH)
    elif env == 'DEVELOPMENT':
        app.config.from_pyfile(config.DEVELOPMENT_CONFIG_PATH)
    else:
        app.config.from_pyfile(config.PRODUCTION_CONFIG_PATH)

    # Initialize the Flask extensions.
    db.init_app(app)
    v1_api.init_app(app)

    return app
