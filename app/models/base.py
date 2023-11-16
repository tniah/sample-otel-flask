# -*- coding: utf-8 -*-
"""Implements base/mixin models for database models."""
import json

from sqlalchemy import Column, DateTime, func, Text

from app.extensions import db


class BaseModel(db.Model):
    """Base class used for database models."""
    __abstract__ = True


class DateTimeMixin:
    """Mixin class used for database models. It adds datetime fields
    to all model classes that subclass it."""
    # pylint: disable=not-callable
    created_at = Column('created_at', DateTime, default=func.now())
    updated_at = Column(
        'updated_at', DateTime,
        default=func.now(), onupdate=func.now())


class DataMixin:
    """Mixin class used for database models. It adds `data` model field
    to all model classes that subclass it."""
    _data = Column('data', Text)

    @property
    def data(self):
        """Get the value of the `data` model field."""
        if self._data:
            return json.loads(self._data)
        return {}

    @data.setter
    def data(self, value):
        """Set the value to the `data` model field."""
        value = value or {}
        self._data = json.dumps(value)