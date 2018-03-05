#! /usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import Decimal

import paypalrestsdk
from tornado.log import app_log
from tornado.concurrent import run_on_executor, futures

from config import Config

__all__ = ['PayPalClient', 'PayPalService']


# ====================================================================
# 业务部分 ============================================================
# ====================================================================


class PayPalClient(object):

    def __init__(self, mode, client_id, client_secret):
        """ 配置指定的PayPal APP

        :param mode: 这个APP的模式("live"或者"sandbox")
        :param client_id: APP的client_id
        :param client_secret: APP的client_secret
        """
        # 配置指定的PayPal APP
        self.api = paypalrestsdk.Api({
            "mode": mode,
            "client_id": client_id,
            "client_secret": client_secret
        })

    def _payment_create(self, **kwargs):
        """ 创建一个Payment对象

        如果必须传入的参数不存在，会抛出异常
        这个函数的必须传入的参数包括(**其中的类型都使用JSON中的名词描述**):
        :param intent: 字符串,(默认:"sale")
        :param payer: 对象
            - :param payment_method: 枚举类型，代表支付的方法(必须）
        :param redirect_urls: 对象
            - :param return_url: 字符串, 在消费者完成支付后返回的url（必须）
            - :param cancel_url: 字符串，在消费者取消支付后返回的url（必须）
        :param transactions: 数组，包含transaction对象
            - :param transaction: 对象, 代表这次支付的交易对象（必须）
                - :param amount: 对象, 这次购买的总价（必须）
                    - :param currency: 字符串, 货币名称（必须）
                        货币参数只支持ISO-4217标准的三位字符代码,而且PayPal并不支持所有货币。
                        详情请看: https://developer.paypal.com/docs/integration/direct/rest/currency-codes/
                    - :param total: 字符串(必须）
                        代表需要支付的总价格。最大支持10位字符。支持两位小数精度。

        具体API请看：　https://developer.paypal.com/docs/api/payments/
        :return: 返回这个Payment对象
        """
        option = {
            "intent": kwargs.get("payment", "sale"),
            "payer": kwargs.get("payer"),
            "redirect_urls": kwargs.get("redirect_urls"),
            "transactions": kwargs.get("transactions")
        }
        if kwargs.get("experience_profile_id", None) is not None:
            option['experience_profile_id'] = kwargs["experience_profile_id"]
        payment = paypalrestsdk.Payment(option, api=self.api)
        return payment

    def _payment_sent(self, payment):
        """将Payment对象发送给PayPal，根据返回的结果作处理

        :param payment: Payment对象
        :return: 根据是否成功，返回信息
        """
        status = {}
        if payment.create():
            status['error'] = 0
            status['message'] = u'成功发送Payment'
        else:
            status['error'] = 1
            status['message'] = payment.error
        return status

    def _payment_redirect(self, payment):
        """将成功发送的Payment解析并获取重定向链接

        :param payment: Payment对象
        :return: 返回重定向链接
        """
        for link in payment.links:
            if link.rel == 'approval_url':
                # 转换为str来避免一些unicode问题
                approval_url = str(link.href)
                return approval_url

    def _payment_execute(self, payment_id, payer_id):
        """验证支付是否完成(静态方法)

        :param payment_id: 在重定向回到本站点后包含在query string的参数
        :param payer_id: 在重定向回到本站点后包含在query string的参数
        :return:返回Payment是否执行完成
        """
        status = {}
        # 根据payment_id来获取payment
        payment = paypalrestsdk.Payment.find(payment_id, api=self.api)

        # 通过payer_id来执行payment
        if payment.execute({"payer_id": payer_id}):
            status['error'] = 0
            status['message'] = u"Payment执行成功"
            status['payment_id'] = payment_id
            status['transaction_id'] = (payment['transactions'][0]
                                               ['related_resources'][0]
                                               ['sale']['id'])
        else:
            status['error'] = 1
            status['message'] = payment.error
        return status

    def _traverse_web_profile_id(self, name):
        all_web_profile = paypalrestsdk.WebProfile.all(api=self.api)
        # all_web_profile为空时，是一个.Resource资源
        if not isinstance(all_web_profile,list):
            if not all_web_profile.to_dict():
                return None
        for web_profile in all_web_profile:
            if web_profile['name'] == name:
                return web_profile['id']
        return None

    def _web_profile_create(self, **kwargs):
        web_profile_obj = paypalrestsdk.WebProfile({
            "name": kwargs.get("name"),
            "input_fields": {
                "allow_note": True,
                "no_shipping": 1,
                "address_override": 1
            },
            "flow_config": {
                "landing_page_type": "billing",
            }
        }, api=self.api)
        if web_profile_obj.create():
            return {"error": 0, "obj": web_profile_obj}
        else:
            return {"error": 1, "message": web_profile_obj.error}


class PayPalService(object):
    executor = futures.ThreadPoolExecutor()
    paypal_client = PayPalClient(
        mode=Config.PAYPAL_CONFIG['client_info']['mode'],
        client_id=Config.PAYPAL_CONFIG['client_info']['client_id'],
        client_secret=Config.PAYPAL_CONFIG['client_info']['client_secret']
    )

    @classmethod
    @run_on_executor
    def checkout(cls, size, quantity, total):
        """用户结账"""
        # 查找是否web profile对象已经创建
        web_profile_name = Config.PAYPAL_CONFIG['webprofile']
        web_profile_id = (cls.paypal_client
                             ._traverse_web_profile_id(web_profile_name))
        if web_profile_id is None:
            # 创建新的web profile对象
            web_profile_info = (cls.paypal_client
                                   ._web_profile_create(name=web_profile_name))
            if web_profile_info['error'] != 0:      # 发生错误
                return web_profile_info
            web_profile_obj = web_profile_info['obj']
            web_profile_id = web_profile_obj.id

        transaction_info = cls._get_transactions_info(size, quantity, total)
        payment_info = {
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": Config.PAYPAL_CONFIG['redirect_urls']
                                                  ['return_url'],
                "cancel_url": Config.PAYPAL_CONFIG['redirect_urls']
                                                  ['cancel_url']
            },
            "transactions": transaction_info,
            "experience_profile_id": web_profile_id
        }
        # 创建payment对象
        payment_obj = cls.paypal_client._payment_create(**payment_info)
        # 发送payment对象
        status = cls.paypal_client._payment_sent(payment_obj)
        if status['error'] != 0:    # 发生错误
            return status
        # 获取重定向URL
        redirect_url = cls.paypal_client._payment_redirect(payment_obj)
        status['redirect_url'] = redirect_url
        status['payment_id'] = payment_obj['id']
        return status

    @classmethod
    @run_on_executor
    def order_execute(cls, payment_id, payer_id):
        """这是一个支付执行的代理函数，在它的上面加上了@run_on_executor装饰器"""
        result = cls.paypal_client._payment_execute(payment_id=payment_id,
                                                    payer_id=payer_id)
        return result

    @classmethod
    def _get_transactions_info(cls, size, quantity, total):
        """生成交易信息"""
        transactions = [{
            "item_list": {
                "items": [{
                    "name": "legging " + str(size),
                    "sku": "LG001",
                    "price": "19.99",
                    "currency": "USD",
                    "quantity": quantity
                }]},
            "amount": {
                "total": str(total),
                "currency": "USD"
            },
            "description": "niceline legging"
        }]
        return transactions

    @classmethod
    def _get_total_price(cls, quantity, unit_price='19.99'):
        total_price = Decimal(unit_price) * quantity
        return total_price
