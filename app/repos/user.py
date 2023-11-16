# -*- coding: utf-8 -*-
"""This module implements User repository."""
from app.models.user import UserModel
from app.repos.base import BaseRepository


class UserRepository(BaseRepository):
    """Implement the User repository."""
    db_model = UserModel
