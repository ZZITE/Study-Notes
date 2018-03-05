#! /usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import quote

from tornado import gen


from .base import BaseHandler
from models.base import Session
from models.business import OrderStatusEnum
from service.paypal import PayPalService
from service.business import BusinessService
from forms.business import EmailForm, OrderForm
from config import Config

__all__ = ['TransitionHandler', 'IndexHandler', 'OrderSubmitHandler',
           'OrderCompletedHandler', 'InformationHandler', 'SuccessHandler',
           'OrderConfirmHandler']

# ====================================================================
# 业务handler =========================================================
# ====================================================================


class IndexHandler(BaseHandler):
    """首页handler"""

    def get(self):
        self.render("index.html")

    def post(self):
        form = EmailForm(self.request.body_arguments)
        if not form.validate():
            return self.render("index.html", **form.errors)

        email = form.data['email']
        self.set_cookie("email", quote(email))
        tracking_code = self.get_cookie(Config.TRACK_ARG_NAME, None)
        obj = BusinessService.email_save(db_session=self.db,
                                   email=email,
                                   remote_ip=self.request.remote_ip,
                                   tracking_code=tracking_code)
        self.redirect(self.reverse_url("transition"))


class InformationHandler(BaseHandler):

    def get(self):
        self.render("information.html")


class TransitionHandler(BaseHandler):
    """过渡页面handler"""

    def get(self):
        self.render("transition.html")


class SuccessHandler(BaseHandler):
    """付款成功页面handler"""

    def get(self):
        self.render("success.html")


class OrderSubmitHandler(BaseHandler):
    """订单详情页面handler"""

    def get(self):
        error_message = None
        if self.get_query_argument("error", None) == '1':
            error_message = 'Paypal transaction fail, ' \
                            'Failure to deduct money, '\
                            'Please try again'
        self.render("order_detail.html", error_message=error_message)

    @gen.coroutine
    def post(self):
        form = OrderForm(self.request.body_arguments)
        if not form.validate():
            return self.render("order_detail.html", error_message=form.errors)
        # 设置Cookie
        for k, v in form.data.items():
            self.set_cookie(quote(k), quote(v))

        # 生成JSON，调用PayPal API
        quantity = int(form.data['quantity'])
        total = PayPalService._get_total_price(quantity,
                                               unit_price='19.99')
        result = yield PayPalService.checkout(size=form.data['size'],
                                              quantity=quantity,
                                              total=total)
        # 判断PayPal结果
        if result['error'] != 0:
            # 错误处理
            self.logger.error("PayPal支付接口发生错误: {}"
                              .format(result['message']))
            error_message = "PayPal payment checkout error...try late"
            return self.render("order_detail.html",
                               error_message=error_message)
        else:
            try:
                # 订单数据持久化
                tracking_code = self.get_cookie(Config.TRACK_ARG_NAME,
                                                None)
                BusinessService.order_save(db_session=self.db,
                                           tracking_code=tracking_code,
                                           total=total,
                                           remote_ip=self.request.remote_ip,
                                           status=OrderStatusEnum.unpaid,
                                           payment_id=result['payment_id'],
                                           **form.data)
            except Exception as e:
                self.logger.error("订单数据库存储发生错误: {}-{}"
                                  .format(type(e).__name__, str(e)))
                error_message = "order save error...try late"
                return self.render("order_detail.html",
                                   error_message=error_message)
            else:
                # 重定向到PayPal的链接
                self.redirect(result['redirect_url'])


class OrderCompletedHandler(BaseHandler):
    """订单完成回调Handler"""

    @gen.coroutine
    def get(self):
        payment_id = self.get_query_argument("paymentId")
        payer_id = self.get_query_argument("PayerID")

        order_obj = BusinessService.get_obj_by_payment_id(db_session=self.db,
                                                          payment_id=payment_id)
        order_id = order_obj.id
        self.db.close()

        if order_obj is None:
            return self.write_error(404)
        if order_obj.status != OrderStatusEnum.unpaid:
            # 用户已经支付, 这次是刷新支付成功页面...
            return self.redirect(self.reverse_url("success"))

        result = yield PayPalService.order_execute(payment_id=payment_id,
                                                   payer_id=payer_id)
        if result['error'] != 0:
            self.redirect(self.reverse_url("order:submit") + "?error=1")
        else:
            # 可能是一个长时间挂起的连接，所以使用多个数据库连接session
            db_session = Session()
            BusinessService.order_executed(db_session=db_session,
                                       order_id=order_id,
                                       transaction_id=result['transaction_id'])
            try:
                db_session.commit()
            except Exception as e:
                self.logger.critical("订单状态持久化发生错误: {}-{}"
                                     .format(type(e).__name__, str(e)))
                db_session.rollback()
            finally:
                db_session.close()
            # 支付成功页面
            self.redirect(self.reverse_url("success"))


class OrderConfirmHandler(BaseHandler):
    """订单确认handler"""

    def get(self, *args, **kwargs):
        """取到token,把订单状态改为'completed'"""
        code = kwargs.get('conde')
        BusinessService.order_confirm(
            self.db,
            code
        )

        self.redirect(self.reverse_url('index'))

