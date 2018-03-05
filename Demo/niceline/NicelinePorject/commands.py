#! /usr/bin/env python
# -*- coding: utf-8 -*-
from six.moves import input
import os
from getpass import getpass

from tornado.options import define, options
from tornado.log import app_log

from tqdm import tqdm

from models import *
from service.admin import AdminService

# 服务器配置
define("host", type=str, default="0.0.0.0", group="server",
       help='定义服务器使用的host', metavar='host')
define("port", type=int, default=8000, group="server",
       help='定义服务器使用的端口', metavar='端口号')
define("start", type=bool, default=False, group="server",
       help="启动服务器")
define("debug", type=bool, group="server", default=False, metavar="bool",
       help="开启debug模式")


# 数据库操作
define("db_reset", type=bool, default=False, group='db',
       help='数据库重置(如果存在数据，慎用)')
define("db_create_all", type=bool, default=False, group="db",
       help='创建所有定义了ORM映射的表')
define("db_create", default=None, group='db', multiple=True,
       help="创建单个或多个表(必须定义ORM-Base类)", metavar="表1,表2...")
define("db_drop", default=None, group='db', multiple=True,
       help='删除单个或多个表(必须定义ORM-Base类)', metavar='表1,表2...')

define("create_superuser", type=bool, default=False, group="account",
       help='创建一个超级管理员帐号')
define("gen_orderno", type=bool, default=False,
       help='生成订单号码')


def db_reset():
    """重置数据库"""
    for metadata in [Base.metadata, NativeBase.metadata]:
        metadata.drop_all()
        metadata.create_all()
        app_log.info("删除表: {}".format(list(metadata.tables.keys())))
        app_log.info("创建表: {}".format(list(metadata.tables.keys())))
    with context_session() as session:
        AdminService.register(session,
                              'nice1',
                              'sdi37f723rwER2')
        app_log.info("创建账号: nice1::sdi37f723rwER2")


def db_create_all():
    """创建所有定义了ORM映射的类"""
    for metadata in [Base.metadata, NativeBase.metadata]:
        metadata.create_all()
        app_log.info("创建表: {}".format(list(metadata.tables.keys())))
    #TODO: 做一些初始化数据插入


def db_create(table_names):
    """创建单个或多个表"""
    tables = dict(Base.metadata.tables)
    tables.update(NativeBase.metadata.tables)
    for table_name, table_obj in tables.items():
        if table_name in table_names:
            table_obj.create()
            app_log.info("创建表: {}".format(table_name))


def db_drop(table_names):
    """删除单个表或多个表"""
    tables = dict(Base.metadata.tables)
    tables.update(NativeBase.metadata.tables)
    for table_name, table_obj in tables.items():
        if table_name in table_names:
            table_obj.drop()
            app_log.info("删除表: {}".format(table_name))


def create_user(is_superuser=None):
    """创建用户帐号"""
    print("用户名:5-36位长度,\n密码:8-36位长度, 首字符必须为字母\n")
    username = input("请输入用户名: ")
    password = getpass("请输入密码: ")
    with context_session() as session:
        data = AdminService.register(session, username, password,
                                     is_superuser)
    print('')
    print(data['message'])


def gen_orderno():
    with context_session() as session:
        all_obj = session.query(OrderModel).all()
        for obj in tqdm(all_obj):
            obj.order_no = obj.created_time.strftime("%Y%m%d") + \
                            "-" +\
                            str(obj.id)
            session.add(obj)


def parse_command_line():
    """这个模块的主函数, 通过调用它使定义的命令生效"""
    options.parse_command_line()

    # 用户帐号操作管理
    if options.create_superuser:
        create_user(is_superuser=True)
    # 数据库操作管理
    if options.db_reset is True:
        db_reset()
    if options.db_create:
        db_create(options.db_create)
    if options.db_drop:
        db_drop(options.db_drop)
    if options.db_create_all:
        db_create_all()
    if options.gen_orderno:
        gen_orderno()
