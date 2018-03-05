#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tornado.web
from handlers import *

BASE_PATH = os.path.dirname(__file__)
CUSTOM_IMAGES_PATH = os.path.join(BASE_PATH, "static")


url_patterns = [
    (r"/", IndexHandler, {}, "index"),
    (r"/transition", TransitionHandler, {}, "transition"),
    (r"/order/submit", OrderSubmitHandler, {}, "order:submit"),
    (r"/order/completed", OrderCompletedHandler, {}, "order:completed"),
    (r"/order/confirm/(?P<code>.+)",
     OrderConfirmHandler, {},
     'order:confirm'),
    (r"/information", InformationHandler, {}, "information"),
    (r"/success", SuccessHandler, {}, "success"),

    (r"/a4min/login", AdminLoginHandler, {}, "admin:login"),
    (r"/a4min/logout", AdminLogoutHandler, {}, "admin:logout"),
    # 订单管理
    (r"/a4min/order", OrderListHandler, {}, "admin:order:list"),
    (r"/a4min/order/(\d+)", OrderDetailHandler, {}, "admin:order:detail"),
    # 订单管理:上传物流信息
    (r"/a4min/order/tracking-no/upload",
     OrderTrackingNoUploadHandler, {},
     'admin:order:upload-tracking-no'),
    # 输出订单为excel文件格式
    (r"/a4min/order/export",
     OrderExportHandler, {},
     "admin:order:export"),
    # 邮件管理
    (r"/a4min/email", EmailListHandler, {}, "admin:email:list"),
    (r"/a4min/email/(\d+)", EmailDetailHandler, {}, "admin:email:detail"),
    # 追踪号码管理
    (r"/a4min/tracking",
     TrackingCodeListHandler, {},
     "admin:tracking:list"),
    (r"/a4min/tracking/(\d+)",
     TrackingCodeDetailHandler, {},
     "admin:tracking:detail"),
    (r"/a4min/tracking/create",
     TrackingCodeCreateHandler, {},
     "admin:tracking:create"),
    # 系统管理
    (r"/a4min/sys-config", SysConfigHandler, {}, "admin:sys-config"),

    (r"/(images/facebook_share1\.jpg)",
     tornado.web.StaticFileHandler,
     dict(path=CUSTOM_IMAGES_PATH)),
]

