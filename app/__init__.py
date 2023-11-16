# -*- coding: utf-8 -*-
"""Entry point for the application."""


def create_app(env=None):
    """Create the Flask app instance that is used throughout the application.

    Args:
        env: Specify the environment in which the Flask application is running
             such as development, production, testing.
    """
    # pylint: disable=import-outside-toplevel
    from app import main

    return main.create_app(name='otel-flask', env=env)
