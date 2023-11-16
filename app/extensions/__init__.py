# -*- coding: utf-8 -*-
"""This module holds Flask extensions."""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.extensions.flask_api import Api

db = SQLAlchemy()
v1_api = Api(
    version='1.0',
    title='Internal Api v1.0 Specification',
    description='Internal Api v1.0 Specification',
    doc='/docs')
migrate = Migrate()
