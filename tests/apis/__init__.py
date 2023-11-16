# -*- coding: utf-8 -*-
import pytest

from tests.apis.factory import Factory


class BaseTest:
    test_client = None
    factory = None

    @pytest.fixture(autouse=True)
    def setup_test(self, test_client, db):
        self.test_client = test_client
        self.factory = Factory(db.session)
