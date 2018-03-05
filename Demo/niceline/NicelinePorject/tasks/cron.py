#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""定时任务"""
from datetime import timedelta

from celery import group
from celery.utils.log import get_task_logger

from models.base import context_session
from models.business import EmailModel, EmailInformRecord
from .app import celery_client
from .mail import *


__all__ = ['check_mail_send', 'test',
           'setup_periodic_tasks']

logger = get_task_logger(__name__)

# ===============================================================
# 定时任务规划 ====================================================
# ===============================================================


@celery_client.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(timedelta(hours=6),
                             check_mail_send.s(),
                             name='check email every 6 hours')

    # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, check_mail_send.s('world'), expires=10)


# ===============================================================
# Celery定时任务 =================================================
# ===============================================================


@celery_client.task
def check_mail_send():
    """检查邮件的发送情况

    如果发现该发送的邮件但是没有发送的情况，重新发送该邮件
    """
    with context_session() as session:
        all_email_list = session.query(
            EmailModel
        ).all()

        no_email_1_list = []
        for email_obj in all_email_list:
            if email_obj.retry and email_obj.retry > 10:    # 重试次数大于１０次，不再发送
                continue
            email_1_sent = False
            # 检查第一封邮件的发送情况
            for record_obj in email_obj.inform_record_set:
                if record_obj.email_name == '1.html':
                    email_1_sent = True
            if email_1_sent is False:
                no_email_1_list.append(email_obj)
                email_obj.retry += 1
                session.add(email_obj)

            # TODO: 检查第二封信的发送情况
            for order_obj in email_obj.inform_record_set:
                pass

        group([send_greet_mail.s(obj.id)
               for obj in no_email_1_list]).apply_async()




