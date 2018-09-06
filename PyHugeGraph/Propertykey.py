# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     Propertykey.py
   Description :
   Author :       tangjiawei
   date:          2018/08/23
-------------------------------------------------
   Change Activity:
                   2018/08/23: v1
-------------------------------------------------
"""


class Propertykey:
    def __init__(self, name, data_type, cardinality, properties=[], user_data={}):
        self.name = name
        self.data_type = data_type
        self.cardinality = cardinality
        self.properties = properties
        self.user_data = user_data

