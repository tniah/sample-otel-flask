# -*- coding: utf-8 -*-
"""User resources for version 1 of the API."""
from flask_restx import Resource

from app.apis.v1.resources.base import ResourceMixin
from app.apis.v1.schemas.user import UserCreateSchema
from app.apis.v1.schemas.user import UserUpdateSchema
from app.lib.decorators import consumes
from app.lib.decorators import pagination
from app.lib.decorators import use_args
from app.lib.definitions import HTTP_STATUS_CODE_CREATED
from app.lib.definitions import HTTP_STATUS_CODE_NO_CONTENT
from app.lib.errors import BadRequestError
from app.repos.user import UserRepository as UserRepo


class UserListResource(Resource, ResourceMixin):
    """Resource to get list of users."""

    @pagination
    def get(self, page, page_size):
        """Handles GET request to the resource.

        Returns:
            List of users.
        """
        total, users = UserRepo.list(page=page, page_size=page_size)
        meta = {
            'pagination': {
                'page': page,
                'pageSize': page_size,
                'total': total
            }
        }
        return self.to_json(users, many=True, meta=meta)

    @consumes('application/json')
    @use_args(UserCreateSchema)
    def post(self, payload):
        """Handles POST request to the resource

        Returns:
            Newly-created user.
        """
        if UserRepo.exists(username=payload['username']):
            raise BadRequestError(message='Username has already been taken')

        user = UserRepo.save(**payload)
        return self.to_json(user, status_code=HTTP_STATUS_CODE_CREATED)


class UserResource(Resource, ResourceMixin):
    """Resource to get a single user from the datastore."""

    def get(self, user_id):
        """Handles GET request to the resource.

        Args:
            user_id: The unique identifier of the user to retrieve.
        Returns:
            User object.
        """
        user = self.get_user_by_id(user_id, raise_exp=True)
        return self.to_json(user)

    @consumes('application/json')
    @use_args(UserUpdateSchema)
    def patch(self, payload, user_id):
        """Handles PATCH request to the resource.

        Args:
            payload: HTTP body of the request.
            user_id: The unique identifier of the user to update.
        Returns:
            User object.
        """
        user = self.get_user_by_id(user_id, raise_exp=True)
        user = UserRepo.update(user, **payload)
        return self.to_json(user)

    def delete(self, user_id):
        """Handles DELETE  request to the resource.

        Args:
            user_id: The unique identifier of the user to delete.
        """
        UserRepo.delete_by_id(id=user_id, synchronize_session=False)
        return '', HTTP_STATUS_CODE_NO_CONTENT
