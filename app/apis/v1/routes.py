# -*- coding: utf-8 -*-
"""URL routes for API resources."""
from flask import Blueprint

from app.apis.v1.resources import *
from app.extensions import v1_api as api

routes = [
    {
        'name': 'User',
        'description': 'Operations about User',
        'path': '/users',
        'resources': [
            (UserListResource, ''),
            (UserResource, '/<string:user_id>')
        ]
    }
]
blueprint = Blueprint('v1_api', __name__, url_prefix='/api/v1')
api.init_app(blueprint)
