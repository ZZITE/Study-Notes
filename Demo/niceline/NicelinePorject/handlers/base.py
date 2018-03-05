#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from urllib.parse import urlparse, urlencode, urlsplit
import traceback

import user_agents
from tornado import web, log, httpclient
from tornado.concurrent import futures
from tornado.httpclient import HTTPError

from service.business import BusinessService
from service.admin import SysConfig
from models.base import Session
from config import Config

__all__ = ["BaseHandler", "LoginRequireMixin"]


# ====================================================================
# 基类和mixin==========================================================
# ====================================================================


class BaseHandler(web.RequestHandler):

    def write_error(self, status_code, **kwargs):
        """Override to implement custom error pages.

        ``write_error`` may call `write`, `render`, `set_header`, etc
        to produce output as usual.

        If this error was caused by an uncaught exception (including
        HTTPError), an ``exc_info`` triple will be available as
        ``kwargs["exc_info"]``.  Note that this exception may not be
        the "current" exception for purposes of methods like
        ``sys.exc_info()`` or ``traceback.format_exc``.
        """
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            self.set_header('Content-Type', 'text/plain')
            for line in traceback.format_exception(*kwargs["exc_info"]):
                self.write(line)
            self.finish()
        else:
            message = kwargs.get("message", None)
            if message:
                self.finish(message)
            else:
                self.finish("<html><title>%(code)d: %(message)s</title>"
                            "<body>%(code)d: %(message)s</body></html>" % {
                                "code": status_code,
                                "message": self._reason,
                            })

    def get_page_arg(self):
        """获取分页参数"""
        page_num = self.get_query_argument("page", 1)
        try:
            page_num = int(page_num)
        except:
            page_num = 1
        return page_num

    def prepare(self):
        # 处理tracking_code
        tracking_code = self.get_query_argument(Config.TRACK_ARG_NAME, None)
        if tracking_code is not None:
            result = BusinessService.tracking_code_process(
                self.db,
                tracking_code=tracking_code,
                remote_ip=self.request.remote_ip
            )
            if result:
                if self.get_cookie(Config.TRACK_ARG_NAME, None) is None:
                    self.set_cookie(Config.TRACK_ARG_NAME,
                                    tracking_code)

    def set_cookie(self, name, value, domain=None, expires=None, path="/",
                   expires_days=None, **kwargs):
        if not expires_days:
            expires_days = Config.COOKIE_EXPIRE
        super(BaseHandler, self).set_cookie(name, value, domain, expires,
                                            path, expires_days, **kwargs)

    def render(self, template_name, **kwargs):
        template_name = self._get_render_template_name(template_name)
        super(BaseHandler, self).render(template_name, **kwargs)

    def _get_render_template_name(self, template_name):
        """根据情况选择模板目录

        如果UA是移动端，选择m文件夹
        另外后台提供了一个模板目录的选项，这个模板目录将会"template_name"头部追加一个目录
        """
        client_user_agent = self.request.headers.get('User-Agent')
        if not template_name.startswith("admin"):
            if client_user_agent:
                user_agent = user_agents.parse(client_user_agent)
                if user_agent.is_mobile:
                    template_name = os.path.join("m", template_name)
            # 根据配置选择模板目录
            template_name = os.path.join(SysConfig.template_dir(),
                                         template_name)
        return template_name

    def reverse_url(self, name, *args, **kwargs):
        """重写了reverse_url方法，让它可以返回绝对url

        :param name: urlSpec对象的name属性
        :param args:
        :param kwargs: 如果关键字参数中存在abs，则返回绝对路径
        :return: 返回相对路径或绝对路径
        """
        relative_url = super(BaseHandler, self).reverse_url(name, *args)
        if kwargs.get("abs", None) is not None:
            abs_url = (self.request.protocol + "://" +
                       self.request.host + relative_url)
            return abs_url
        return relative_url

    def initialize(self):
        # 懒加载属性
        self._db = None
        self._thread_pool = None
        self._process_pool = None
        self._async_client = None
        self.logger = log.access_log

    @property
    def async_client(self):
        if self._async_client is None:
            return self._get_async_client()
        return self._async_client

    def _get_async_client(self):
        return httpclient.AsyncHTTPClient()

    @property
    def process_pool(self):
        if self._process_pool is None:
            return self._get_process_pool()
        return self._process_pool

    def _get_process_pool(self):
        self._process_pool = futures.ProcessPoolExecutor()
        return self._process_pool

    @property
    def thread_pool(self):
        if self._thread_pool is None:
            return self._get_thread_pool()
        return self._thread_pool

    def _get_thread_pool(self):
        self._thread_pool = futures.ThreadPoolExecutor()
        return self._thread_pool

    @property
    def db(self):
        if self._db is None:
            return self._get_db()
        return self._db

    def _get_db(self):
        self._db = Session()
        return self._db

    def on_finish(self):
        # 数据库事务commit
        if self._db:
            try:
                self._db.commit()
            except Exception as e:
                self.logger.error("数据库commit错误: {}".format(str(e)),
                                  exc_info=True)
                self._db.rollback()
            finally:
                self._db.close()


class LoginRequireMixin(object):
    """一个覆盖了RequestHandler.prepare，实现登录要求的Mixin"""
    def prepare(self):
        super(LoginRequireMixin, self).prepare()
        if not self.current_user:
            if self.request.method in ("GET", "HEAD"):
                url = self.get_login_url()
                if "?" not in url:
                    if urlsplit(url).scheme:
                        # if login url is absolute, make next absolute too
                        next_url = self.request.full_url()
                    else    :
                        next_url = self.request.uri
                    url += "?" + urlencode(dict(next=next_url))
                self.redirect(url)
                return
            raise HTTPError(403)

