#! /usr/bin/env python
# -*- coding: utf-8 -*-
from wtforms_tornado import Form
from wtforms import (StringField, TextAreaField, DateField,
                     IntegerField, SelectField, BooleanField)
from wtforms.validators import DataRequired

from models.business import OrderStatusEnum


class TrackingForm(Form):
    campaign_name = StringField("活动名称",
                                validators=[DataRequired()],
                                render_kw={
                                    "required": True,
                                    "placeholder": "活动名称"
                                })
    campaign_description = TextAreaField("活动描述",
                                         render_kw={
                                             "placeholder": "活动描述",
                                             "rows": 8
                                         })
    code = StringField("追踪代码",
                       validators=[DataRequired()],
                       render_kw={
                           "required": True,
                           "placeholder": "追踪代码"
                       })


class OrderForm(Form):
    # 只读表单
    email = StringField("邮箱",
                        render_kw={
                            "readonly": True,
                        })
    remote_ip = StringField("IP地址",
                            render_kw={
                                "readonly": True
                            })
    payment_id = StringField("Payment ID",
                             render_kw={
                                 "readonly": True
                             })
    transaction_id = StringField("Transaction ID",
                                 render_kw={
                                    "readonly": True
                                 })
    order_no = StringField("订单编号",
                           render_kw={
                               'readonly': True
                           })
    total = StringField("总价",
                        render_kw={
                            "readonly": True
                        })
    firstName = StringField("first name",
                            validators=[DataRequired()],
                            render_kw={
                                "required": True
                            })
    lastName = StringField("last name",
                           validators=[DataRequired()],
                           render_kw={
                            "required": True
                           })
    address = StringField("address",
                          validators=[DataRequired()],
                          render_kw={
                            "required": True
                          })
    state = StringField("state",
                        validators=[DataRequired()],
                        render_kw={
                            "required": True
                        })
    country = StringField("country",
                          validators=[DataRequired()],
                          render_kw={
                              "required": True
                          })
    zipcode = StringField("zipcode",
                          validators=[DataRequired()],
                          render_kw={
                              "required": True
                          })
    size = StringField("尺寸",
                       validators=[DataRequired()],
                       render_kw={
                            "required": True
                       })
    quantity = IntegerField("数量",
                            validators=[DataRequired()],
                            render_kw={
                                "required": True
                            })
    phone = StringField("电话号码")
    tracking_no = StringField("快递单号")
    donated = BooleanField("是否已捐款",
                           render_kw={
                               "style": "font-size: 20px;"
                           })
