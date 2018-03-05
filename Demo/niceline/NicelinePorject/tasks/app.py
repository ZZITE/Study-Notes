#! /usr/bin/env python
# -*- coding: utf-8 -*-

from celery import Celery


celery_client = Celery(__name__,
                       broker="redis://:Womenstore123098!@127.0.0.1:6379/0",
                       backend='redis://:Womenstore123098!@127.0.0.1:6379/0',
                       include=['tasks.mail', 'tasks.cron'])



if __name__ == '__main__':
    celery_client.start()
