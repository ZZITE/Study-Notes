# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import event, and_

from .business import OrderStatusEnum
from .business import (EmailLoginRecord, EmailInformRecord,
                       OrderOperationRecordModel,
                       OrderModel)

__all__ = ['send_email_after_order_successful',
           'send_email_after_record_insert',
           'add_order_no_column']


# ====================================================================
# 监听事件 ============================================================
# ====================================================================

@event.listens_for(EmailLoginRecord, "after_insert")
def send_email_after_record_insert(mapper, connection, target):
    """在新增访问记录时，查看是否对该邮箱发送了第一封邮件1.html，如果没有则发送"""
    engine_string = str(connection.engine)
    if 'niceline_test' in engine_string:
        return

    result = (connection.execute(EmailInformRecord.__table__.select()
         .where(and_(EmailInformRecord.__table__.c.email_id == target.email_id,
                     EmailInformRecord.__table__.c.email_name == '1.html'))))
    result_row = result.fetchone()
    if result_row is None:
        from tasks.mail import send_greet_mail
        send_greet_mail.apply_async((target.email_id, ),
                                    countdown=10)


@event.listens_for(OrderOperationRecordModel, "after_insert")
def send_email_after_order_successful(mapper, connection, target):
    """在订单完成后发送一封邮件
    订单完成的标志就是插入了订单对象操作记录new_status = paid
    """
    engine_string = str(connection.engine)
    if 'niceline_test' in engine_string:
        return

    if target.new_status == OrderStatusEnum.paid:
        from tasks.mail import send_order_success_mail
        send_order_success_mail.apply_async((target.order_id, ),
                                            countdown=10)


@event.listens_for(OrderModel, 'after_insert')
def add_order_no_column(mapper, connection, target):
    """在一个订单创建后自动生成订单编号

    订单编号的生成规则是'订单日期-订单ID'
    """
    order_no = target.created_time.strftime("%Y%m%d") + "-" + str(target.id)
    target_table = OrderModel.__table__
    stmt =target_table.update().\
            where(target_table.c.id == target.id).\
            values(order_no=order_no)
    connection.execute(stmt)


@event.listens_for(OrderOperationRecordModel, 'after_insert')
def send_order_shipped_email(mapper, connection, target):
    """如果发现订单状态变为"shipped"，发送一封通知邮件

    但是如果出现下面的情况不会发送:
        1. 处于测试模式
        2. 原来就是shipped状态
        3. 没有更新订单追踪号码
        4. 已经发送过该邮件
    """
    engine_string = str(connection.engine)
    if 'niceline_test' in engine_string:
        return
    if target.old_status == OrderStatusEnum.shipped:
        return
    if not target.order.tracking_no:
        return

    for inform_obj in target.order.owner.inform_record_set:
        if inform_obj.email_name == "3.html":
            return

    # send email
    from tasks.mail import send_order_shipped_email
    send_order_shipped_email.apply_async(
        (target.order.id,),
        countdonw=10
    )



