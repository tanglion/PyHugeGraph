#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: tanglion
# Mail: tanglion1987@163.com
# Created Time:  2018-9-13 9:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name = "PyHugeGraph",
    version = "0.1.0",
    keywords = ("pip", "hugegraph","PyHugeGraph"),
    description = "HugeGraph Python API Package",
    long_description = "HugeGraph Python API Package",
    license = "Apache Licence",

    url = "https://github.com/tanglion/PyHugeGraph",
    author = "tanglion",
    author_email = "tanglion1987@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["requests","json"]
)