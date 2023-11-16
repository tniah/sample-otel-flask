# -*- coding: utf-8 -*-
"""This module implements the User model."""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.extensions import bcrypt
from app.models.base import BaseModel
from app.models.base import DataMixin
from app.models.base import DateTimeMixin


class UserModel(BaseModel, DateTimeMixin, DataMixin):
    """Implements the User model."""
    __tablename__ = 'users'

    # Attributes
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String(255), nullable=False, unique=True)
    fullname = Column('fullname', String(255), nullable=True)
    _password = Column('password', String(255), nullable=False)
    is_active = Column('is_active', Boolean, default=True)

    def __init__(self, username, password, fullname=None, is_active=True,
                 data=None):
        """Initialize the User object.

        Args:
            username: Username must be a unique identifier.
            fullname: Fullname of the User.
            password: The password of the User.
            is_active: Default to True.
            data: User metadata in a dictionary.
        """
        self.username = username
        self.password = password
        self.fullname = fullname
        self.is_active = is_active
        self.data = data

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = bcrypt.generate_password_hash(value)
