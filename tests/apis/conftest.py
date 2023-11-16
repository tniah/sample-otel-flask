# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope='function')
def test_client(app):
    ctx = app.test_request_context()
    ctx.push()
    c = app.test_client()
    yield c
    ctx.pop()


@pytest.fixture(scope='function', autouse=True)
def auto_use_db_session(db_session):
    pass
