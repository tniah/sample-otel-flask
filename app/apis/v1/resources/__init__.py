# -*- coding: utf-8 -*-'
"""This module holds version 1 of the API.

The API exposes the following resources:
"""

from app.apis.v1.resources.user import UserListResource
from app.apis.v1.resources.user import UserResource

__all__ = [
    'UserListResource', 'UserResource'
]
