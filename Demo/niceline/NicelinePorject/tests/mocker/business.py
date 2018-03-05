#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


from models import *


def add_new_order(n, created_time=None):
    with context_session() as session:
        if created_time is None:
            created_time = datetime.datetime.now()
        for i in range(n):
            order_obj = OrderModel(
                firstName="firstName{0}".format(i),
                lastName='lastName{0}'.format(i),
                zipcode='zipcode{0}'.format(i),
                city='city{0}'.format(i),
                state='state{0}'.format(i),
                country='country{0}'.format(i),
                phone='phone{0}'.format(i),
                size='L',
                quantity=1,
                email='{0}@example.com'.format(i),
                status=OrderStatusEnum.unpaid,
                created_time=created_time
            )
            session.add(order_obj)


if __name__ == '__main__':
    created_time = datetime.datetime.now() - datetime.timedelta(days=30)
    add_new_order(100, created_time)
