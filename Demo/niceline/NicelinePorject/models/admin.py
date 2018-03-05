#! /usr/bin/env python
# -*- coding: utf-8 -*-
from hashlib import md5

from sqlalchemy import Column, String, Boolean

from .base import Base

__all__ = ['AdminUser', 'SysConfigModel']


class AdminUser(Base):
    __tablename__ = 'admin_user'
    username = Column(String(32),
                      unique=True,
                      nullable=False,
                      index=True)
    password = Column(String(32),
                      nullable=False)
    salt = Column(String(8),
                  nullable=False)
    is_superuser = Column(Boolean,
                          default=False)

    def verify_password(self, input_password):
        """验证密码是否正确"""
        secret_password = AdminUser.generate_secret_password(input_password,
                                                             self.salt)
        return secret_password == self.password

    @staticmethod
    def generate_secret_password(password, salt):
        """生成一个加密密码"""
        password = password.encode()
        salt = salt.encode()
        password = md5(password).hexdigest().encode()
        return md5(password + b"|HM|" + salt).hexdigest()


class SysConfigModel(object):
    """一个以redis为基础的model"""
    key = 'niceline:sysconfig'
    template_dir = 'template_dir'
    email_dir = 'email_dir'


