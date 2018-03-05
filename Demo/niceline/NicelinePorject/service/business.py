#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json

from sqlalchemy import bindparam, func

from models.business import *
from models.base import bakery, redis_cli

__all__ = ['BusinessService']



class BusinessService(object):

    @classmethod
    def tracking_code_process(cls, db_session, tracking_code, remote_ip):
        """处理tracking_code
        如果这个值存在于数据库，则为它增量click并返回True
        否则返回False

        :param remote_ip: 用户ip，每个ip的访问频率是受限的
        :param tracking_code: 追踪码,`TrackingCodeModel.code`
        :return: 根据结果返回布尔值
        """
        redis_key = "tracking:{0}:{1}".format(tracking_code, remote_ip)
        if redis_cli.exists(redis_key):
            return False

        obj = (db_session.query(TrackingCodeModel)
                         .filter_by(code=tracking_code)
                         .one_or_none())
        if obj is not None:
            obj.clicks += 1
            redis_cli.set(redis_key, 1)
            redis_cli.expire(redis_key, 30 * 60)        # 每半小时只能点击一次
            return True
        return False

    @classmethod
    def email_save(cls, db_session, **kwargs):
        """将首页输入的email信息持久化到数据库,
        如果已经存在，则更新这条记录.否则，创建新的一条记录.

        :param email: email地址
        :param remote_ip: 用户当前的ip地址
        """
        obj = (db_session.query(EmailModel)
                         .filter(EmailModel.email == kwargs['email'])
                         .first())
        if not obj:
            obj = EmailModel(email=kwargs['email'])
            db_session.add(obj)
            db_session.flush()
        if kwargs.get('tracking_code', None) is not None:
            # 如果用户是通过tracking引流而来，为它们建立关联
            tracking_id = (db_session.query(TrackingCodeModel.id)
                                     .filter_by(code=kwargs['tracking_code'])
                                     .scalar())
            obj.tracking_id = tracking_id
        record_obj = EmailLoginRecord(remote_ip=kwargs['remote_ip'])
        obj.record_set.append(record_obj)
        db_session.add(obj)
        return obj

    @classmethod
    def order_save(cls, db_session, **kwargs):
        """保存订单信息"""
        email = kwargs['email']
        tracking_code = kwargs.pop('tracking_code', None)
        email_obj = (db_session.query(EmailModel)
                            .filter_by(email=email)
                            .one_or_none())
        if email_obj is None:
            email_obj = cls.email_save(db_session,
                                       email=email,
                                       remote_ip=kwargs['remote_ip'],
                                       tracking_code=tracking_code)
        obj = OrderModel(**kwargs)
        email_obj.order_set.append(obj)
        db_session.add(email_obj)
        # 如果持久化到刷新出现错误，则下面的步骤(跳转支付)没必要继续了
        db_session.flush()

    @classmethod
    def get_obj_by_payment_id(cls, db_session, payment_id):
        """根据payment_id获取订单信息"""
        obj = (db_session.query(OrderModel)
                         .filter(OrderModel.payment_id == payment_id)
                         .first())
        return obj

    @classmethod
    def order_executed(cls, db_session, order_id, transaction_id):
        """order payment执行成功"""
        order_obj = db_session.query(OrderModel).get(order_id)
        if order_obj:
            cls._order_update(db_session, order_obj,
                              status=OrderStatusEnum.paid,
                              transaction_id=transaction_id)

    @classmethod
    def change_order_status(cls, db_session, order_id, status, user_id=None):
        if isinstance(status, str):
            status = getattr(OrderStatusEnum, status)
        order_obj = db_session.query(OrderModel).get(order_id)
        if order_obj:
            cls._order_update(db_session,
                              order_obj,
                              status=status,
                              user_id=user_id)

    @classmethod
    def _order_update(cls, db_session, order_obj, user_id=None, **kwargs):
        """ order表的记录更新, 在每次更新时会创建一个新的"order_operation_record"记录

        :param db_session:
        :param order_obj:
        :param kwargs: 最少需要包含status
        :return:
        """
        old_status = order_obj.status
        new_status = kwargs.pop("status")
        other_changes = {}
        # 其实加入一个before_update钩子更好
        for key, value in kwargs.items():
            if getattr(order_obj, key) != value:
                setattr(order_obj, key, value)     # 顺带更新order_obj
                other_changes[key] = value

        other_changes_json = json.dumps(other_changes,
                                        ensure_ascii=False)
        record_obj = OrderOperationRecordModel(old_status=old_status,
                                               new_status=new_status,
                                               other_changes=other_changes_json,
                                               user_id=user_id)

        order_obj.status = new_status
        order_obj.record_set.append(record_obj)
        db_session.add(order_obj)

    @classmethod
    def order_deliver_upload(cls, db_session, user_id, order_no, tracking_no):
        """根据order_no找到订单对象并更新tracking_no字段
        并且将订单状态调整为已发货
        """
        order_obj = db_session.query(
            OrderModel
        ).filter(
            OrderModel.order_no == order_no
        ).one_or_none()
        if order_no is not None and order_obj is not None:
            cls._order_update(db_session, order_obj, user_id,
                              tracking_no=tracking_no,
                              status=OrderStatusEnum.shipped)

    @classmethod
    def order_data_export(cls, db_session, start_date, end_date,
                          status, user_id=None):
        """订单数据导出"""
        baked_query = bakery(lambda session: session.query(OrderModel))
        if start_date:
            baked_query += lambda q: q.filter(
                func.date(OrderModel.created_time) >= bindparam('start_date')
            )
        if end_date:
            baked_query += lambda q: q.filter(
                func.date(OrderModel.created_time) <= bindparam('end_date')
            )
        if status:
            baked_query += lambda q: q.filter(
                OrderModel.status == bindparam('status')
            )
        result = baked_query(db_session).params(
            start_date=start_date,
            end_date=end_date,
            status=(getattr(OrderStatusEnum, status)
                    if status else None)
        ).all()

        for obj in result:
            # 如果订单"已支付"，自动改为"处理中"
            if obj.status == OrderStatusEnum.paid:
                cls._order_update(db_session, obj, user_id,
                                  status=OrderStatusEnum.processing)
        return result

    @classmethod
    def order_confirm(cls, db_session, code):
        order_obj = db_session.query(
            OrderModel
        ).filter(
            OrderModel.confirm_code == code
        ).one_or_none()

        if order_obj and \
                order_obj.status != OrderStatusEnum.completed:
            cls._order_update(
                db_session,
                order_obj,
                status=OrderStatusEnum.completed
            )
