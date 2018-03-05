#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.testing import AsyncHTTPTestCase

from server import Application
from config import settings
from .base import HTTPClientMixin


class AdminAPITestCase(HTTPClientMixin, AsyncHTTPTestCase):

    def get_app(self):
        return Application(settings)

    def reverse_url(self, *args, **kwargs):
        abs = kwargs.pop('abs', False)
        url = self._app.reverse_url(*args, **kwargs)
        if abs is True:
            return self.get_url(url)
        return url

    def fetch(self, *args, **kwargs):
        response = super(AdminAPITestCase, self).fetch(*args, **kwargs)
        response._body = response.body.decode("utf-8")
        return response

    def test_admin_login_fail(self):
        url = self.reverse_url("admin:login")
        post_data = {
            "username": "fake",
            "password": "invalidpassword"
        }
        response = self.post(url, data=post_data)
        self.assertEqual(response.effective_url, self.get_url(url))
        self.assertIn("重新输入", response.body)

    def test_access_order_list(self):
        url = self.reverse_url("admin:order:list")
        response = self.get(url)
        self.assertEqual(response.effective_url, self.get_url(url))
        self.assertIn("尺寸", response.body)


