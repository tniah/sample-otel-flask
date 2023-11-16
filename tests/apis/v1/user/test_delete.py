# -*- coding: utf-8 -*-
from app.lib.definitions import HTTP_STATUS_CODE_NO_CONTENT
from app.lib.definitions import HTTP_STATUS_CODE_NOT_FOUND
from tests.apis import BaseTest


class TestUserResourceDelete(BaseTest):
    ENDPOINT = '/api/v1/users'

    def test_delete_user(self):
        user = self.factory.user.create()
        user_id = user.id
        resp = self.test_client.delete(f'{self.ENDPOINT}/{user_id}')
        assert resp.status_code == HTTP_STATUS_CODE_NO_CONTENT
        assert resp.data == b''

        resp = self.test_client.get(f'{self.ENDPOINT}/{user_id}')
        assert resp.status_code == HTTP_STATUS_CODE_NOT_FOUND
