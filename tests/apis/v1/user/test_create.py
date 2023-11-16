# -*- coding: utf-8 -*-
from app.lib.definitions import HTTP_STATUS_CODE_CREATED
from tests.apis import BaseTest


class TestUserListResourcePost(BaseTest):
    ENDPOINT = '/api/v1/users'

    def test_create_user(self):
        payload = {
            'username': 'makai',
            'password': 'my_password',
            'fullname': 'Makai'
        }
        resp = self.test_client.post(self.ENDPOINT, json=payload)
        assert resp.status_code == HTTP_STATUS_CODE_CREATED
        data = resp.json.get('data')
        assert all(data[k] == data[k] for k in payload if k != 'password')
        assert not data.get('password')
