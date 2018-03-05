#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.concurrent import futures
from tornado.testing import AsyncTestCase, gen_test
from paypalrestsdk import Payment

from service.paypal import PayPalClient


class PayPalTestCase(AsyncTestCase):
    @classmethod
    def setUpClass(cls):
        cls.paypal_client = PayPalClient(
            mode='sandbox',
            client_id='AduMrSVpBpufHUUZN_PNzRf5kBCSBxOKPlFYHDjSv9EbxPrRwXgMmbyaIpA1r5U2bixBi2XtZ7rtNPdU',
            client_secret='EMqbZ1SvnbGRGBMK-SvvEEW4oT9B_0BdOzerpLUKVUcqGSEqfc-edoBP7RwKnzuBlLr-whyDU2EpTTQH'
        )
        cls.executor = futures.ThreadPoolExecutor()
        cls.async_do = cls.executor.submit

    @gen_test(timeout=15)
    def test_payment_sent(self):
        init_data = {
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": "http://localhost:8000/order/completed",
                "cancel_url": "http://localhost:8000/order/canceled"
            },
            "transactions": [{
                "amount": {
                    "currency": "USD",
                    "total": "5.00"
                }
            }]
        }
        payment_obj = self.paypal_client._payment_create(**init_data)
        self.assertIsInstance(payment_obj, Payment)
        status = yield self.async_do(self.paypal_client._payment_sent, payment_obj)
        self.assertEqual(status['error'], 0)

    @gen_test(timeout=15)
    def test_payment_error_arg_can_not_sent(self):
        init_data = {
            "error": {
                "nothing": "mock data"
            }
        }
        payment_obj = self.paypal_client._payment_create(**init_data)
        status = yield self.async_do(self.paypal_client._payment_sent, payment_obj)
        self.assertNotEqual(status['error'], 0)

    @gen_test(timeout=25)
    def test_payment_redirect(self):
        init_data = {
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": "http://localhost:8000/order/completed",          # TODO: 改为config中的配置值
                "cancel_url": "http://localhost:8000/order/canceled"
            },
            "transactions": [{
                "amount": {
                    "currency": "USD",
                    "total": "5.00"
                }
            }]
        }
        payment_obj = self.paypal_client._payment_create(**init_data)
        self.assertIsInstance(payment_obj, Payment)
        status = yield self.async_do(self.paypal_client._payment_sent, payment_obj)
        self.assertEqual(status['error'], 0)
        redirect_url = self.paypal_client._payment_redirect(payment_obj)
        self.assertTrue(redirect_url.startswith("http"))
