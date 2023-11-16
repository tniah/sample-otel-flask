# -*- coding: utf-8 -*-
import pytest

from app import create_app
from app.extensions import db as _db


@pytest.fixture(scope='session')
def app():
    return create_app(env='test')


@pytest.fixture(scope='session', autouse=True)
def db(app):
    with app.app_context():
        _db.create_all()
        _db.session.commit()
        yield _db
        _db.session.remove()
        _db.drop_all()


@pytest.fixture(scope='function')
def db_session(db, app):
    with app.app_context():
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        yield db.session
        db.session.rollback()
