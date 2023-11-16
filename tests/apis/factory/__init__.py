# -*- coding: utf-8 -*-
from tests.apis.factory.user import UserFactory


class Factory:

    def __init__(self, db_session):
        self.db_session = db_session
        self.user = UserFactory(self)
