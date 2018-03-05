#! /usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum as EnumBase

from sqlalchemy import (Column, String, Integer, Numeric, Enum,
                        Boolean, Text, ForeignKey, Date)
from sqlalchemy.orm import relationship, backref

from .base import Base

__all__ = ['EmailModel', 'OrderModel', 'EmailLoginRecord',
           'OrderOperationRecordModel', "OrderStatusEnum",
           'DonateTicketModel', 'TrackingCodeModel']


class OrderStatusEnum(EnumBase):
    """订单状态的枚举类"""
    unpaid = 0
    paid = 1
    processing = 2
    shipped = 3
    completed = 4
    abandon = 5
    deleted = 6


# ====================================================================
# 数据表 ==============================================================
# ====================================================================


class EmailModel(Base):
    __tablename__ = 'login_email'

    email = Column(String(128),
                   index=True)
    retry = Column(Integer)

    tracking_id = Column(Integer, ForeignKey("tracking_code.id"))


class EmailLoginRecord(Base):
    __tablename__ = 'login_email_record'

    remote_ip = Column(String(32),
                       index=True)

    email_id = Column(Integer, ForeignKey("login_email.id"))
    email = relationship(EmailModel,
                         backref=backref("record_set",
                                         cascade="all, delete-orphan"))


class EmailInformRecord(Base):
    __tablename__ = 'email_inform_record'

    email_name = Column(String(32))
    order_id = Column(Integer, nullable=True)
    token = Column(String(64), nullable=True)

    email_id = Column(Integer, ForeignKey("login_email.id"))
    email = relationship(EmailModel,
                         backref=backref("inform_record_set",
                                         cascade="all, delete-orphan"))


class OrderModel(Base):
    __tablename__ = 'order'

    email = Column(String(128),
                   index=True)
    order_no = Column(String(64))
    tracking_no = Column(String(256))
    remote_ip = Column(String(32),
                       index=True)
    firstName = Column(String(32))
    lastName = Column(String(32))
    address = Column(String(256))
    state = Column(String(32))
    city = Column(String(32))
    country = Column(String(32))
    zipcode = Column(String(32))
    size = Column(String(8))
    quantity = Column(Integer)
    total = Column(Numeric(8, 2))
    status = Column(Enum(OrderStatusEnum))
    payment_id = Column(String(128))
    transaction_id = Column(String(128))
    phone = Column(String(32))
    donated = Column(Boolean, default=False)
    confirm_code = Column(String(50))

    email_id = Column(Integer, ForeignKey("login_email.id"))
    owner = relationship(EmailModel,
                         backref='order_set')

    def fullname(self):
        return self.firstName + " " + self.lastName


class OrderOperationRecordModel(Base):
    __tablename__ = 'order_operation_record'

    old_status = Column(Enum(OrderStatusEnum))
    new_status = Column(Enum(OrderStatusEnum))
    other_changes = Column(Text)
    user_id = Column(Integer, nullable=True)

    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship(OrderModel,
                         backref=backref("record_set",
                                         cascade='all, delete-orphan'))


class TrackingCodeModel(Base):
    __tablename__ = 'tracking_code'

    campaign_name = Column(String(32))
    campaign_description = Column(Text)
    code = Column(String(36))
    clicks = Column(Integer, default=0)

    email_set = relationship(EmailModel,
                             backref="tracking_by")

    def order_count(self):
        count = 0
        except_status = [
            OrderStatusEnum.unpaid,
            OrderStatusEnum.abandon,
            OrderStatusEnum.deleted
        ]
        for email_obj in self.email_set:
            for order_obj in email_obj.order_set:
                if order_obj.status not in except_status:
                    count += 1
        return count


class DonateTicketModel(Base):
    __tablename__ = 'donate_ticket'

    payment_id = Column(String(128))
    transaction_id = Column(String(128))
    user_list = Column(Text)
    image = Column(String(128))



