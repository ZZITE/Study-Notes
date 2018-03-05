#! /usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import urlencode

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from tornado.testing import AsyncTestCase, AsyncHTTPTestCase

from selenium import webdriver

from models import *
from server import Application


class DBTestCase(AsyncTestCase):
    @classmethod
    def setUpClass(cls):
        # TODO: 改为配置参数
        engine_string = "mysql+pymysql://phpmyadmin:durex123@" \
                        "192.168.0.145:3306"\
                        "/niceline_test?" \
                        "charset=utf8"
        cls.engine = create_engine(engine_string,
                                   pool_recycle=3600,
                                   pool_size=3600)
        cls.Session = scoped_session(sessionmaker(bind=cls.engine))

    def setUp(self):
        super().setUp()
        Base.metadata.create_all(bind=self.engine)
        self.db = self.Session()

    def tearDown(self):
        super().tearDown()
        self.db.close()
        self.Session.remove()
        Base.metadata.drop_all(bind=self.engine)

    def db_commit(self):
        self.db.commit()


class ClientBaseTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return Application()

    def reverse_url(self, *args, **kwargs):
        abs = kwargs.pop('abs', False)
        url = self._app.reverse_url(*args, **kwargs)
        if abs is True:
            return self.get_url(url)
        return url

    def setUp(self):
        super(ClientBaseTestCase, self).setUp()
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("network.proxy.type", 0)
        self.browser = webdriver.Firefox(
            executable_path='/root/selenium_driver/geckodriver',
            firefox_binary='/usr/local/firefox/firefox',
            firefox_profile=firefox_profile
        )
        self.browser.implicitly_wait(3)

    def tearDown(self):
        super(ClientBaseTestCase, self).tearDown()
        self.browser.quit()


class HTTPClientMixin(object):
    headers = {
    "Cookie": """
      user_id=2|1:0|10:1513684710|7:user_id|4:MQ==|aa54c6b720376172c4ebb778cc544bb07e6d536ae0b50c2fc9aba143423ab44a
      """.strip()
    }

    def get(self, url, data=None, headers=None):
        if headers is None:
            headers = self.headers
        else:
            headers.update(self.headers)
        if data is not None:
            if isinstance(data, dict):
                data = urlencode(data)
            if '?' in url:
                url += '&amp;%s' % data
            else:
                url += '?%s' % data
        return self.fetch(url, method='GET', headers=headers)

    def post(self, url, data, headers=None):
        if headers is None:
            headers = self.headers
        else:
            headers.update(self.headers)
        if data is not None:
            if isinstance(data, dict):
                data = urlencode(data)
        return self.fetch(url, method='POST', body=data, headers=headers)
