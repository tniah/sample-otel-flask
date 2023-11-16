# -*- coding: utf-8 -*-
"""This module implements base/mixin schema classes for API schema classes."""
from marshmallow import EXCLUDE
from marshmallow import Schema as _Schema


class Schema(_Schema):
    """Base schema class for API schema classes."""

    class Meta:
        """Options object for a Schema."""
        unknown = EXCLUDE
