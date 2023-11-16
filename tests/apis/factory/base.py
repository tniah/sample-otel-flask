# -*- coding: utf-8 -*-
from faker import Faker


class BaseFactory:

    def __init__(self, factory):
        self.factory = factory
        self.db_session = factory.db_session
        self.faker = Faker()

    def commit(self, obj):
        self.db_session.add(obj)
        self.db_session.commit()
