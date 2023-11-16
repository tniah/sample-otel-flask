# -*- coding: utf-8 -*-
from app.lib.definitions import HTTP_STATUS_CODE_OK
from tests.apis import BaseTest


class TestUserResourceGet(BaseTest):
    ENDPOINT = '/api/v1/users'

    def test_get_user(self):
        user = self.factory.user.create()
        resp = self.test_client.get(f'{self.ENDPOINT}/{user.id}')
        assert resp.status_code == HTTP_STATUS_CODE_OK
        assert resp.json.get('code') == HTTP_STATUS_CODE_OK
        assert resp.json.get('message') == 'OK'
        data = resp.json.get('data')
        assert data.get('id') == user.id
        assert data.get('username') == user.username
        assert not data.get('password')
