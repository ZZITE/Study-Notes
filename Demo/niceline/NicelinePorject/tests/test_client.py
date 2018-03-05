#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""使用selenium来实现功能测试"""
from tornado.testing import gen_test

from .base import ClientBaseTestCase


class ClientTestCase(ClientBaseTestCase):
    @gen_test
    def test_admin_login(self):
        login_url = self.reverse_url("admin:login", abs=True)

        self.browser.get(login_url)

