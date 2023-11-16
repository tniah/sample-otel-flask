# -*- coding: utf-8 -*-
from app.models.user import UserModel
from tests.apis.factory.base import BaseFactory


class UserFactory(BaseFactory):

    def create(self, username=None, fullname=None, password=None,
               is_active=True):
        user = UserModel(
            username=username or self.faker.user_name(),
            password=password or self.faker.password(),
            fullname=fullname or self.faker.name(),
            is_active=is_active)
        self.commit(user)
        return user
