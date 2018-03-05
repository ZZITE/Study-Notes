#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""发送邮件的任务"""

import os
import uuid
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

from tornado.template import Template

from celery.utils.log import get_task_logger

from .app import celery_client
from config import Config, BASE_PATH
from models import context_session
from models.business import EmailInformRecord, EmailModel, OrderModel
from service.admin import SysConfig

__all__ = ['MailClient', 'send_order_success_mail', 'send_greet_mail',
           'send_order_shipped_email']

logger = get_task_logger(__name__)


class MailClient(object):
    """邮件发送客户端"""

    @staticmethod
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    @classmethod
    def _message_create(cls, from_, to, subject, content, type='html'):
        """消息对象的生成

        :param from_: 寄信人
        :param to: 收件者
        :param subject: 标题
        :param content: 内容
        :param type: 邮件的mimetype, 默认为"html"
        :return: MIMEText对象
        """
        from_ = "{0} <{1}>".format(Config.EMAIL_SENDER, from_)
        msg = MIMEText(content, type, "utf-8")
        msg['From'] = cls._format_addr(from_)
        msg['To'] = Header(to, 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8').encode()
        return msg

    @classmethod
    def _mail_send(cls, from_addr, to_addr, msg,
                  smtp_server, smtp_port, password):
        """邮件发送

        :param from_addr: 发件人的邮箱地址
        :param to_addr: 收信人(多人)的邮箱地址(可迭代对象)
        :param msg: 一个email.MIMEText对象
        :param smtp_port: smtp端口
        :param smtp_server: smtp服务器
        :return:
        """

        # 建立和smtp服务器的连接并登录
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        # server.set_debuglevel(1)
        # server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()

    @classmethod
    def send_mail(cls, to, subject, content):
        # 创建邮件msg对象
        from_ = Config.SMTP_USERNAME
        msg_obj = cls._message_create(from_,
                                      to,
                                      subject,
                                      content)
        # 发送邮件
        cls._mail_send(from_, [to], msg_obj,
                       Config.SMTP_SERVER,
                       Config.SMTP_PORT,
                       Config.SMTP_PASSWORD)

# ===============================================================
# Celery任务 =====================================================
# ===============================================================


@celery_client.task(bind=True)
def send_greet_mail(self, email_obj_id):
    """发送欢迎邮件"""
    with context_session() as session:
        exists_query = (session.query(EmailInformRecord)
                            .filter_by(email_id=email_obj_id,
                                       email_name='1.html')
                            .exists())
        if session.query(exists_query).scalar() is True:
            return
        # 还没有发送过1.html邮件
        try:
            email_obj = session.query(EmailModel).get(email_obj_id)
            with open(os.path.join(
                    BASE_PATH,
                    'templates',
                    "email",
                    SysConfig.email_dir(),
                    "1.html"
            ), "r") as f:
                content = f.read()
            MailClient.send_mail(email_obj.email,
                                 "Thank you for your concern",
                                 content)
        except Exception as exc:
            raise self.retry(exc=exc)
        else:
            record_obj = EmailInformRecord(
                email_name='1.html',
                email_id=email_obj_id,
            )
            session.add(record_obj)
            logger.info("欢迎邮件[1]发送成功, 目标:{!s}".format(email_obj.email))


@celery_client.task(bind=True)
def send_order_success_mail(self, order_obj_id, transaction_id=None):
    """发送订单支付成功的邮件"""
    with context_session() as session:
        order_obj = session.query(OrderModel).get(order_obj_id)
        exists_query = (session.query(EmailInformRecord)
                        .filter_by(email_id=order_obj.email_id,
                                   email_name='2.html',
                                   order_id=order_obj.id)
                        .exists())
        if session.query(exists_query).scalar() is True:
            return

        # 还没有发送过该邮件
        try:
            with open(
                os.path.join(
                    BASE_PATH,
                    'templates',
                    "email",
                    SysConfig.email_dir(),
                    "2.html"
            ),"r") as f:
                template_obj = Template(f.read())
            # 生成并发送邮件
            content = template_obj.generate(
                        customer_name=order_obj.fullname(),
                        size=order_obj.size,
                        quantity=order_obj.quantity,
                        total=order_obj.total,
                        payment_id=order_obj.payment_id,
                        transaction_id=(transaction_id
                                        if transaction_id is not None
                                        else order_obj.transaction_id)
                      )
            MailClient.send_mail(order_obj.email,
                                 "Thank you for your donation and support",
                                 content)
        except Exception as exc:
            raise self.retry(exc=exc)
        else:
            record_obj = EmailInformRecord(
                email_name='2.html',
                order_id=order_obj.id,
                email_id=order_obj.email_id,
            )
            session.add(record_obj)
            logger.info("订单成功邮件[2]发送成功，目标: {!s}, 订单id: {!s}".format(
                order_obj.email, order_obj.id
            ))


@celery_client.task(bind=True)
def send_order_shipped_email(self, order_id):
    """在订单发货以后发送邮件"""
    with context_session() as session:
        order_obj = session.query(OrderModel).get(order_id)
        exists_query = (session.query(EmailInformRecord)
                        .filter_by(email_id=order_obj.email_id,
                                   email_name='3.html',
                                   order_id=order_obj.id)
                        .exists())
        if session.query(exists_query).scalar() is True:
            return

        try:
            with open(
                os.path.join(
                    BASE_PATH,
                    'templates',
                    "email",
                    SysConfig.email_dir(),
                    "3.html"
            ),"r") as f:
                template_obj = Template(f.read())
            confirm_code = str(uuid.uuid4())

            content = template_obj.generate(
                customer_name=order_obj.fullname(),
                tracking_no=order_obj.tracking_no,
                confirm_code=confirm_code
            )
            MailClient.send_mail(order_obj.email,
                                 "Donation order progress notifications",
                                 content)
        except Exception as exc:
            raise self.retry(exc=exc)

        else:
            record_obj = EmailInformRecord(
                email_name='3.html',
                order_id=order_obj.id,
                email_id=order_obj.email_id,
            )
            order_obj.confirm_code = confirm_code
            session.add_all([record_obj, order_obj])
            logger.info("发货提醒邮件[3]发送成功，目标: {!s}, 订单ID: {!s}".format(
                order_obj.email, order_obj.id
            ))
