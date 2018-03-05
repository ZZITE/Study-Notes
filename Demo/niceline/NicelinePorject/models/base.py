#! /usr/bin/env python
# -*- coding: utf-8 -*-
from contextlib import contextmanager
from datetime import datetime

from redis import StrictRedis

from sqlalchemy import Column, Integer, DateTime, create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext import baked
from sqlalchemy.ext.hybrid import hybrid_property

from config import Config


# ====================================================================
# 数据库配置 ===========================================================
# ====================================================================

db_info = {
    "db_dialect": Config.DB_DIALECT if Config.DB_DIALECT is not None else "mysql",
    "db_username": Config.DB_USERNAME,
    "db_password": Config.DB_PASSWORD,
    "db_host": Config.DB_HOST if Config.DB_HOST is not None else "localhost",
    "db_port": Config.DB_PORT if Config.DB_PORT is not None else 3306,
    "db_dbname": (Config.DB_DBNAME if Config.DB_DBNAME is not None
                                    else "webshell_manager"),
    "db_charset": Config.DB_CHARSET if Config.DB_CHARSET is not None else "utf8"
}


if Config.DB_DIALECT == 'mysql':
    engine_string = ('{db_dialect}+pymysql://{db_username}'
                     ':{db_password}@{db_host}:{db_port}/{db_dbname}'
                     '?charset={db_charset}'
                        .format(**db_info))
elif Config.DB_DIALECT == 'sqlite':
    engine_string = ("{db_dialect}:///{base_path}/{db_dbname}.sq3?"
                     "check_same_thread=False"
                      .format(base_path=Config.BASE_PATH, **db_info))

engine = create_engine(engine_string,
                       pool_recycle=3600,
                       pool_size=3600)


class BaseClass(object):
    """一个Base对象的基类"""
    id = Column(Integer,
                primary_key=True)
    created_time = Column(DateTime,
                          default=datetime.now,
                          index=True)
    modified_time = Column(DateTime,
                           onupdate=datetime.now,
                           default=datetime.now)

    @hybrid_property
    def created_date(self):
        return self.created_time.date()

    @created_date.expression
    def created_date(self):
        return func.date(self.created_time)

# =================================================================
# model related object ============================================
# =================================================================


Base = declarative_base(bind=engine,
                        cls=BaseClass)

NativeBase = declarative_base(bind=engine)              # 一般用于多对多表

Session = sessionmaker(bind=engine)

bakery = baked.bakery()

redis_cli = StrictRedis(password='Womenstore123098!',
                        decode_responses=True)

# ==================================================================
# utils callable ===================================================
# ==================================================================


@contextmanager
def context_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class Cache(object):
    base_key = 'cache:{0}'
    expire = 600

    @classmethod
    def set(cls, key, content):
        redis_key = cls.base_key.format(key)
        redis_cli.set(redis_key, content)
        if cls.expire:
            redis_cli.expire(redis_key, cls.expire)

    @classmethod
    def get(cls, key):
        return redis_cli.get(cls.base_key.format(key))

    @classmethod
    def delete(cls, key):
        redis_cli.delete(cls.base_key.format(key))