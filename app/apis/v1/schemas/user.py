# -*- coding: utf-8 -*-
from marshmallow import fields
from marshmallow import validate

from app.apis.v1.schemas.base import Schema


class UserSchema(Schema):
    """This class to serialize a user database model to JSON."""
    id = fields.Integer()
    username = fields.String()
    fullname = fields.String()
    is_active = fields.Boolean(data_key='isActive')
    created_at = fields.DateTime(data_key='createdAt')
    updated_at = fields.DateTime(data_key='updatedAt')

    class Meta(Schema.Meta):
        dump_only = ('id',)


class UserCreateSchema(Schema):
    """This class to validate input data when creating a new user."""
    username = fields.String(
        required=True,
        validate=validate.Length(min=3, max=50))
    fullname = fields.String(allow_none=True)
    password = fields.String(
        required=True,
        validate=validate.Length(min=5, max=255))


class UserUpdateSchema(Schema):
    """This class to validate input data when updating the user."""
    fullname = fields.String(allow_none=True)
    password = fields.String(
        required=True,
        validate=validate.Length(min=5, max=255))
    is_active = fields.Boolean(
        truthy={True}, falsy={False}, data_key='isActive')
