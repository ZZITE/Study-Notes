#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

# 项目根路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# 数据库配置
DB_DIALECT = 'mysql'
DB_DBNAME = "niceline"
DB_USERNAME = 'phpmyadmin'
DB_PASSWORD = 'durex123'
DB_HOST = '192.168.0.145'
DB_PORT = 3306
DB_CHARSET = 'utf8'

# email配置
SMTP_SERVER = 'smtp.exmail.qq.com'
SMTP_PORT = '465'
SMTP_USERNAME ='service@niceline.com'
SMTP_PASSWORD = 'Jnbnic20170501@'
EMAIL_SENDER = 'NiceLine'


# SMTP_SERVER = 'smtp.gmail.com'
# SMTP_PORT = '587'
# SMTP_USERNAME ='bnm965321@gmail.com'
# SMTP_PASSWORD = 'zhoudxsn1'
# EMAIL_SENDER = 'NiceLine-Community'


# SMTP_SERVER = 'smtp.qq.com'
# SMTP_PORT = '587'
# SMTP_USERNAME ='289184595@qq.com'
# SMTP_PASSWORD = 'ghmsaxhfzcribidd'
# EMAIL_SENDER = 'NiceLine-Community'

# COOKIE过期时间(单位:天)
COOKIE_EXPIRE = 1

# 分页中每页显示的数量
NUM_PER_PAGE = 50

# tracking code的配置
TRACK_ARG_NAME = 'tracking'            # tracking的GET参数名, 同样用于cookie


# 沙盒环境
PAYPAL_CONFIG = {
    "webprofile": "niceline-checkout",      # webprofile的名称
    "client_info": {
        "mode": 'sandbox',
        "client_id": 'AduMrSVpBpufHUUZN_PNzRf5kBCSBxOKPlFYHDjSv9EbxPrRwXgMmbyaIpA1r5U2bixBi2XtZ7rtNPdU',
        "client_secret": 'EMqbZ1SvnbGRGBMK-SvvEEW4oT9B_0BdOzerpLUKVUcqGSEqfc-edoBP7RwKnzuBlLr-whyDU2EpTTQH'
    },
    "redirect_urls": {
        "return_url": "http://localhost:8000/order/completed",
        "cancel_url": "http://localhost:8000/order/submit"
    }
}

# 真实环境
# PAYPAL_CONFIG = {
#     "webprofile": "niceline-checkout",
#     "client_info": {
#         "mode": "live",
#         "client_id": "AcrEjjqzFj4hdWd1YtmB2EzU8kQzH6TiP_UiYXYgLbi-6eZHloJMzQRiYvQPn5YiIBH7OsTbWkj-GzeE",
#         "client_secret": "EApuyiB-2-tKEdkGAJ_Hzea2rBXgcQVMfAHPQUqLy1J75MYrG2-o0u6in7mlpt87Zfh4UxNsJ5JP10T_",
#     },
#     "redirect_urls": {
#         "return_url": "http://www.niceline.com/order/completed",
#         "cancel_url": "http://www.niceline.com/order/submit"
#     }
# }


# application的配置参数
settings = dict(
    debug=False,
    login_url='/a4min/login',
    cookie_secret='hgsdfdsf3qerewqt1wexz4fsdfsdfcdsdsdhjewr',
    # xsrf_cookies=True,
    template_path=os.path.join(BASE_PATH, "templates"),
    static_path=os.path.join(BASE_PATH, "static"),
)


class _Config(object):
    """获得全局配置，如果没有则获取默认值"""
    def __getattr__(self, item):
        value = globals().get(item, None)
        return value if value else None
Config = _Config()