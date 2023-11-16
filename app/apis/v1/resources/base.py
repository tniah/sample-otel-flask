# -*- coding: utf-8 -*-
"""This module implements base/mixin classes for internal API resources."""
from flask import jsonify

from app.apis.v1.schemas.user import UserSchema
from app.lib.definitions import HTTP_STATUS_CODE_CREATED
from app.lib.definitions import HTTP_STATUS_CODE_OK
from app.lib.errors import NotFoundError
from app.repos.user import UserRepository as UserRepo


class ResourceMixin:
    """Mixin for API resources."""
    fields_registry = {
        'users': UserSchema
    }

    def to_json(self, model, schema_cls=None, meta=None,
                many=False, status_code=HTTP_STATUS_CODE_OK):
        """Create JSON response from a database model.

        Args:
            model: Instance of a database model.
            schema_cls: Class that inherits from marshmallow.schema.Schema.
            meta: A dictionary holding any metadata for the result
                  such as pagination.
            many: Should be set to `True` if `model` is a collection
                  so that the `model` will be serialized to a list.
            status_code: Integer used as status_code in the response.

        Returns:
            Response in JSON format (instance of flask.wrappers.Response)
        """
        if many is True:
            schema = {'data': []}
        else:
            schema = {'data': {}}

        if model:
            if not schema_cls:
                try:
                    schema_cls = self.fields_registry[model.__tablename__]
                except AttributeError:
                    schema_cls = self.fields_registry[model[0].__tablename__]

            if many is True:
                schema['data'] = list(schema_cls(many=True).dump(model))
            else:
                schema['data'] = schema_cls(many=False).dump(model)

        if status_code in (HTTP_STATUS_CODE_OK, HTTP_STATUS_CODE_CREATED):
            schema.update({
                'code': status_code,
                'message': 'OK'
            })

        if meta:
            schema.update(meta)
        response = jsonify(schema)
        response.status_code = status_code
        return response

    @staticmethod
    def get_user_by_id(user_id, raise_exp=True):
        """Get a single user by `user_id`.

        Args:
            user_id: The unique identifier of the user.
            raise_exp: Set to `True` if you want to raise an exception
                       when user_id does not exist.

        Returns:
            User object.

        Raises:
            NotFoundError: If user_id does not exist.
        """
        user = UserRepo.get(id=user_id)
        if not user and raise_exp is True:
            raise NotFoundError(message='No user found with this Id')

        return user
