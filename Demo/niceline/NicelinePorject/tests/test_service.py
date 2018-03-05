#! /usr/bin/env python
# -*- coding: utf-8 -*-
from models.business import *
from service.business import BusinessService
from service.admin import *
from .base import DBTestCase


class EmailServiceTestCase(DBTestCase):
    def test_get_object_list_show_order_count(self):
        EmailService.create(self.db,
                            email="123@qq.com")
        BusinessService.order_save(self.db,
                                   email="123@qq.com",
                                   remote_ip='123')
        self.db_commit()
        object_list = EmailService.get_object_list(self.db, 1)
        self.assertEqual(object_list.items[0].order_count, 1)


    def test_get_object_list(self):
        EmailService.create(self.db,
                            email="123@qq.com")
        EmailService.create(self.db,
                            email='456@qq.com')
        result = EmailService.get_object_list(self.db)
        self.assertTrue(result.total, 2)
        self.assertEqual([obj.order_count for obj in result.items], [0, 0])


class OrderServiceTestCase(DBTestCase):
    def test_get_object_list(self):
        OrderService.create(self.db,
                            email='123@qq.com',
                            status=OrderStatusEnum.unpaid)
        OrderService.create(self.db,
                            email='456@qq.com',
                            status=OrderStatusEnum.unpaid)
        result = OrderService.get_object_list(self.db)
        self.assertTrue(result.total, 2)


class DonateServiceTestCase(DBTestCase):
    def test_object_create(self):
        result = DonateService.create(self.db,
                                      payment_id='123',
                                      transaction_id='123',
                                      user_list='a,b,c',
                                      image='fake.png')
        self.assertTrue(result['error'] == 0)

    def test_object_create_fail_by_unique(self):
        DonateService.create(self.db,
                             transaction_id='123')
        result = DonateService.create(self.db,
                                      transaction_id="123")
        self.assertTrue(result['error'] != 0)
        self.assertIn('exists', result['message'])

    def test_object_update(self):
        obj = DonateService.create(self.db,
                                   transaction_id='123')['obj']
        result = DonateService.update(self.db, obj,
                                      transaction='456')
        self.assertTrue(result['error'] == 0)

    def test_object_update_fail_by_unique(self):
        obj1 = DonateService.create(self.db,
                                    transaction_id='123')['obj']
        obj2 = DonateService.create(self.db,
                                    transaction_id='456')['obj']
        result = DonateService.update(self.db, obj1,
                                      transaction_id='456')
        self.assertTrue(result['error'] != 0)
        self.assertIn('exists', result['message'])

    def test_object_delete(self):
        obj1 = DonateService.create(self.db,
                                    transaction_id='123')['obj']
        DonateService.delete(self.db, obj1)
        exists = DonateService.unique_exist(self.db,
                                            obj1.transaction_id)
        self.assertFalse(exists)


class TrackingServiceTestCase(DBTestCase):
    def test_object_create(self):
        result = TrackingService.create(self.db,
                                      code='123')
        self.assertTrue(result['error'] == 0)

    def test_object_create_fail_by_unique(self):
        TrackingService.create(self.db,
                               code='123')
        result = TrackingService.create(self.db,
                                        code="123")
        self.assertTrue(result['error'] != 0)
        self.assertIn('exists', result['message'])

    def test_object_update(self):
        obj = TrackingService.create(self.db,
                                     code='123')['obj']
        result = TrackingService.update(self.db, obj,
                                        code='456')
        self.assertTrue(result['error'] == 0)

    def test_object_update_fail_by_unique(self):
        obj1 = TrackingService.create(self.db,
                                      code='123')['obj']
        obj2 =TrackingService.create(self.db,
                                     code='456')['obj']
        result = TrackingService.update(self.db, obj1,
                                        code='456')
        self.assertTrue(result['error'] != 0)
        self.assertIn('exists', result['message'])

    def test_object_delete(self):
        obj1 = TrackingService.create(self.db,
                                     code='123')['obj']
        DonateService.delete(self.db, obj1)
        exists = TrackingService.unique_exist(self.db,
                                              obj1.code)
        self.assertFalse(exists)


class BusinessServiceTestCase(DBTestCase):

    def test_code_process_fail_by_none(self):
        result = BusinessService.tracking_code_process(
            self.db,
            tracking_code='not exists',
            remote_ip='127.0.0.1'
        )
        self.assertEqual(result, False)

    def test_code_process_success(self):
        obj = TrackingCodeModel(code='123')
        self.db.add(obj)
        self.db_commit()

        result = BusinessService.tracking_code_process(
            self.db,
            tracking_code='123',
            remote_ip='127.0.0.1'
        )
        self.assertEqual(result, True)
        self.assertEqual(obj.clicks, 1)


    def test_email_save(self):
        email = "foo@bar.com"
        remote_ip = "127.0.0.1"
        BusinessService.email_save(self.db,
                                   email=email,
                                   remote_ip=remote_ip)
        self.db_commit()

        email_obj = (self.db.query(EmailModel)
                            .filter(EmailModel.email == email)
                            .one_or_none())
        self.assertTrue(email_obj is not None)

        record_obj = (self.db.query(EmailLoginRecord)
                             .filter(EmailLoginRecord.remote_ip == remote_ip)
                             .one_or_none())
        self.assertTrue(record_obj is not None)

    def test_order_save(self):
        BusinessService.order_save(self.db,
                                   total="19.99",
                                   remote_ip='127.0.0.1',
                                   email='123@qq.com')
        order_obj = (self.db.query(OrderModel)
                            .filter(OrderModel.total == "19.99")
                            .one_or_none())
        self.assertTrue(order_obj.remote_ip == '127.0.0.1')

    def test_order_save_error(self):
        with self.assertRaisesRegex(Exception, r"invalid.*argument"):
            BusinessService.order_save(self.db,
                                       total_amount='a',
                                       email='123@qq.com',
                                       remote_ip='127.0.0.1')

    def test_order_executed(self):
        BusinessService.order_save(self.db,
                                   total="19.99",
                                   email='123@qq.com',
                                   remote_ip='127.0.0.1')
        order_id= (self.db.query(OrderModel.id)
                         .filter(OrderModel.total == "19.99")
                         .scalar())
        BusinessService.order_executed(self.db, order_id, "t_id")
        self.db_commit()

        order_obj = (self.db.query(OrderModel)
                         .filter(OrderModel.total == "19.99")
                         .one_or_none())
        self.assertTrue(order_obj.transaction_id == "t_id")

        record_obj = (self.db.query(OrderOperationRecordModel)
                             .filter_by(order_id=order_obj.id)
                             .one_or_none())
        self.assertTrue(record_obj.new_status == OrderStatusEnum.paid)
        self.assertIn("transaction", record_obj.other_changes)

    def test_order_status_change(self):
        BusinessService.order_save(self.db,
                                   total="19.99",
                                   email='123@qq.com',
                                   remote_ip='127.0.0.1')
        BusinessService.change_order_status(self.db,
                                            order_id=1,
                                            status='paid')
        self.db_commit()

        order_obj = (self.db.query(OrderModel)
                     .filter(OrderModel.total == "19.99")
                     .one_or_none())
        self.assertTrue(order_obj.status.name == "paid")


