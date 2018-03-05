#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tornado import web, ioloop, httpserver
from tornado.log import app_log

from urls import url_patterns
from config import settings
from commands import parse_command_line, options


class Application(web.Application):
    def __init__(self, config):
        super(Application, self).__init__(url_patterns, **config)


if __name__ == '__main__':
    parse_command_line()

    if options.debug:
        settings['debug'] = True

    if options.start:
        app = Application(settings)
        server = httpserver.HTTPServer(app,
                                       xheaders=True)
        server.bind(options.port,
                    options.host)
        server.start()

        app_log.info("服务器启动，监听: \"{}:{}\"".format(options.host,
                                                  options.port))
        ioloop.IOLoop.current().start()