# -*- coding: utf-8 -*-
"""This module implements Python decorators for the application."""
from functools import wraps

from flask import request
from marshmallow import EXCLUDE
from marshmallow import fields
from marshmallow import Schema as _Schema
from marshmallow import validate
from marshmallow import ValidationError

from app.lib.errors import BadRequestError
from app.lib.errors import UnsupportedMediaTypeError
from app.lib.utils import parse_marshmallow_error


def pagination(func):
    """Pagination decorator."""

    class Schema(_Schema):
        page = fields.Integer(
            validate=validate.Range(min=1),
            missing=1)
        page_size = fields.Integer(
            validate=validate.Range(min=1, max=100),
            missing=50)

        class Meta:
            unknown = EXCLUDE

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            params = Schema().load(request.args)
        except ValidationError as e:
            raise BadRequestError(
                message='Validation failed',
                error_details=parse_marshmallow_error(e)) from e

        new_args = args + (params['page'], params['page_size'])
        return func(*new_args, **kwargs)

    return wrapper


def use_args(schema_cls):
    """This decorator is used to inject parsed arguments into a view function
    or method."""

    def decorated(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            arguments = request.args.to_dict()
            if request.is_json:
                arguments.update(request.get_json())

            try:
                payload = schema_cls().load(arguments)
            except ValidationError as e:
                raise BadRequestError(
                    message='Validation failed',
                    error_details=parse_marshmallow_error(e)) from e
            new_args = args + (payload,)
            return func(*new_args, **kwargs)

        return wrapper

    return decorated


def consumes(*content_types):
    """This decorator is used to validate the content type
    of the HTTP request body."""

    def decorated(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mimetype = request.mimetype
            if mimetype not in content_types:
                raise UnsupportedMediaTypeError(
                    message=f'Content type "{mimetype}" is not supported.')

            return func(*args, **kwargs)

        return wrapper

    return decorated
