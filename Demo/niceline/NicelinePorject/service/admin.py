#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
from uuid import uuid4

from tornado.log import gen_log
from sqlalchemy import func
from sqlalchemy_pagination import paginate
from sqlalchemy.ext.hybrid import hybrid_property

from .base import ModelService
from .business import BusinessService
from models.base import redis_cli
from models.business import *
from models.admin import *
from config import Config
from libs.utils import get_random_string

__all__ = ['DonateService', 'TrackingService', 'OrderService', 'EmailService',
           'AdminService', 'SysConfig']

# constants
USER_PATTERN = re.compile(r'\w{5,36}')
PASS_PATTERN = re.compile(r"[A-Za-z][\w\W]{7,36}")


class AdminService(object):

    @classmethod
    def register(cls, db_session, username, password, is_superuser=None):
        if USER_PATTERN.match(username) is None:
            return {'error': 1,
                    "message": "请输入5-36位长度的用户名"}
        if PASS_PATTERN.match(password) is None:
            return {'error': 2,
                    "message": "请输入8-36位长度的密码, 首字符必须为字母"}
        user_exists = db_session.query(AdminUser).filter(
            AdminUser.username == username).one_or_none() is not None
        if user_exists:
            return {"error": 3, "message": "这个用户名已经存在，请重新输入"}
        # 注册
        salt = get_random_string(8)
        secret_password = AdminUser.generate_secret_password(password, salt)
        user_obj = AdminUser(username=username,
                             password=secret_password,
                             salt=salt,
                             is_superuser=is_superuser)
        try:
            db_session.add(user_obj)
            db_session.flush()
        except Exception as e:
            gen_log.error("注册帐号时发生异常: {}".format(str(e)), exc_info=True)
            db_session.rollback()
            return {"error": 4, "message": "数据库发生错误"}
        else:
            return {"error": 0, "message": "注册成功!"}

    @classmethod
    def login(cls, db_session, username, password):
        data = {"error": 1, "message": "用户名或密码错误"}
        user = db_session.query(AdminUser).filter(
            AdminUser.username == username).one_or_none()
        if user is None:
            return data
        if user.verify_password(password):
            data = {"error": 0, "message": "登录成功!", "user_id": str(user.id)}
        return data


class DonateService(ModelService):
    model = DonateTicketModel
    unique = "transaction_id"

    @classmethod
    def get_object_list(cls, db_session, page_num=1):
        """获取donate清单票据对象的列表"""
        object_list = paginate(db_session.query(DonateTicketModel),
                               page_num, Config.NUM_PER_PAGE)
        return object_list


class TrackingService(ModelService):
    model = TrackingCodeModel
    unique = 'code'

    @classmethod
    def get_object_list(cls, db_session, page_num=1):
        """ 获取追踪代码的列表页面数据

        :param db_session:
        :param page_num:
        :return: 返回的字段包括：campaign_name, code, clicks, created_time
        """
        object_query = (db_session.query(cls.model))
        object_list = paginate(object_query, page_num, Config.NUM_PER_PAGE)
        return object_list

    @classmethod
    def gen_unique_code(cls, db_session):
        """生成一个唯一的tracking_code
        """
        code = get_random_string(8)
        exists_query = db_session.query(
            cls.model
        ).filter(
            cls.model.code == code
        ).exists()
        while db_session.query(exists_query).scalar() is True:
            code = get_random_string(8)
        return code


class EmailService(ModelService):
    model = EmailModel

    @classmethod
    def get_object_list(cls, db_session, page_num=1):
        """获取email登录的列表页面

        :param db_session:
        :param page_num:
        :return: 返回的字段包括：email, order_count, created_time
        """
        order_count_query = (db_session.query(func.count(OrderModel.id))
                             .join(cls.model)
                             .filter(OrderModel.email_id == cls.model.id))
        object_query = (db_session.query(cls.model.email,
                                         order_count_query.label('order_count'),
                                         cls.model.created_time))
        object_list = paginate(object_query, page_num, Config.NUM_PER_PAGE)
        return object_list


class OrderService(ModelService):
    model = OrderModel

    @classmethod
    def get_object_list(cls, db_session, page_num=1, filter_=None):
        object_query = (db_session.query(cls.model.id, cls.model.email,
                                         cls.model.order_no,
                                         cls.model.status,
                                         cls.model.size, cls.model.quantity,
                                         cls.model.total, cls.model.remote_ip,
                                         cls.model.created_time)
                                  .filter(cls.model.status != OrderStatusEnum.deleted)
                                  .order_by(cls.model.id.desc()))
        if filter_ is not None:
            if filter_['start_date']:
                object_query = object_query.filter(
                    func.date(cls.model.created_time) >= filter_['start_date']
                )
            if filter_['end_date']:
                object_query = object_query.filter(
                    func.date(cls.model.created_time) <= filter_['end_date']
                )
            if filter_['status']:
                object_query = object_query.filter(
                    cls.model.status == getattr(OrderStatusEnum,
                                                filter_['status'])
                )
        object_list = paginate(object_query, page_num, Config.NUM_PER_PAGE)
        return object_list

    @classmethod
    def delete(cls, db_session, obj, user_id):
        """删除"""
        BusinessService._order_update(db_session, obj,
                                      status=OrderStatusEnum.deleted,
                                      user_id=user_id)
        return cls.db_flush(db_session)
    
    
class SysConfig(object):
    model = SysConfigModel
    
    @classmethod
    def get(cls, key, default=None):
        value = redis_cli.hget(cls.model.key, key)
        if not value and default:
            return default
        return value

    @classmethod
    def set(cls, key, value):
        redis_cli.hset(cls.model.key, key, value)

    @classmethod
    def template_dir(cls, default='v1'):
        return cls.get(cls.model.template_dir, default)

    @classmethod
    def set_template_dir(cls, value):
        return cls.set(cls.model.template_dir, value)

    @classmethod
    def email_dir(cls, default='v1'):
        return cls.get(cls.model.email_dir, default)

    @classmethod
    def set_email_dir(cls, value):
        return cls.set(cls.model.email_dir, value)


