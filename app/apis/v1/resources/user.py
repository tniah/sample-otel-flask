# -*- coding: utf-8 -*-
"""User resources for version 1 of the API."""
from flask_restx import Resource

from app.apis.v1.resources.base import ResourceMixin


class UserListResource(Resource, ResourceMixin):
    """Resource to get list of users."""

    def get(self):
        """Handles GET request to the resource.

        Returns:
            List of users.
        """
        pass

    def post(self):
        """Handles POST request to the resource

        Returns:
            Newly-created user.
        """
        pass


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

    def patch(self, user_id):
        """Handles PATCH request to the resource.

        Args:
            user_id: The unique identifier of the user to update.
        Returns:
            User object.
        """
        pass

    def delete(self, user_id):
        """Handles DELETE  request to the resource.

        Args:
            user_id: The unique identifier of the user to delete.
        """
        pass
