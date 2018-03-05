#! /usr/bin/env python
# -*- coding: utf-8 -*-
import string
import random

def get_random_string(length):
    """生成一个length长度的随机字符串"""
    all_chars = string.ascii_letters + string.digits
    return "".join([random.choice(all_chars) for _ in range(length)])
