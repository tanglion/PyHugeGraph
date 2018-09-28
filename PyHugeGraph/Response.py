# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     Response.py
   Description :
   Author :       tangjiawei
   date:          2018/08/23
-------------------------------------------------
   Change Activity:
                   2018/08/23: v1
-------------------------------------------------
"""


import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class Response(object):
    """
        获得响应内容和状态码
    """
    def __init__(self, status_code, result):
        self.status_code = status_code
        self.response = result

