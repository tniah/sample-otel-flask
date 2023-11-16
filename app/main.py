# -*- coding: utf-8 -*-
"""Entry point for the application."""
import importlib
import os

from flask import Flask
from flask_restx import Namespace

import config
from app.extensions import db
from app.extensions import migrate
from app.extensions import v1_api, bcrypt
from app.lib.errors import ApiHTTPError


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
    db.init_app(app=app)
    v1_api.init_app(app=app)
    migrate.init_app(app=app, db=db)
    bcrypt.init_app(app=app)

    # Setup URL routes for the API
    for module_name in app.config['INSTALLED_MODULES']:
        try:
            module = importlib.import_module(f'{module_name}.routes')
            for ns in getattr(module, 'routes'):
                resources = ns.pop('resources', [])
                ns = Namespace(**ns)
                for rs in resources:
                    rs, endpoint, kwargs = (*rs, {}) if len(rs) == 2 else rs
                    ns.add_resource(rs, endpoint, **kwargs)
                getattr(module, 'api').add_namespace(ns)
            app.register_blueprint(getattr(module, 'blueprint'))
        except (ImportError, AttributeError) as exp:
            raise exp

    # Register error handlers
    @app.errorhandler(ApiHTTPError)
    def handle_api_http_error(error):
        """Error handler for API HTTP errors.

        Returns:
            HTTP response object(instance of flask.wrappers.Response)
        """
        return error.build_response()

    return app
