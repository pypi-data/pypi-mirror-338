#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        logger_object.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 定义“表征`记录器对象`的类”。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2024/11/10     revise
# ------------------------------------------------------------------
# 导包 ==============================================================
import inspect
from .dataframe_utils import create_df_from_dict

# 声明 ==============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
Defining a class that represents `logger object`.
"""

__all__ = [
    "get_properties",
    "LoggerObject",
]


# 定义 ==============================================================
def get_properties0(obj):
    """
    获取对象的所有非私有属性和由`@property`装饰器定义的属性。

    :param obj: 指定的对象。
    :return: 属性键值对组成的字典。
    :rtype: dict
    """
    # 获取对象的所有属性名
    attributes = dir(obj)
    # 初始化一个字典来存储非私有属性及其值
    public_attributes = {}

    for attr in attributes:
        if not attr.startswith("_"):  # 过滤私有属性
            value = getattr(obj, attr)
            if not callable(value):  # 过滤方法和函数
                public_attributes[attr] = value

    return public_attributes


def get_properties(obj):
    """
    获取对象的所有非私有属性和由`@property`装饰器定义的属性。

    :param obj: 指定的对象。
    :return: 属性键值对组成的字典。
    :rtype: dict
    """
    # 获取对象的所有属性名
    attributes = dir(obj)
    # 初始化一个字典来存储非私有属性及其值
    public_attributes = {}

    for attr in attributes:
        if not attr.startswith("_"):
            value = getattr(obj, attr)
            if not callable(value) and (not inspect.isroutine(value)):
                # 检查是否是数据描述符（如 @property）
                if isinstance(getattr(type(obj), attr, None), property):
                    public_attributes[attr] = value
                else:
                    # 如果不是方法或函数，则添加到字典
                    public_attributes[attr] = value

    return public_attributes


class LoggerObject(object):
    """
    类`LoggerObject`表征“记录器对象”。
    """

    def __init__(self):
        """
        类`LoggerObject`的初始化方法。
        目前没有特定的初始化操作，如果后续需要添加初始化逻辑，请在此处实现。
        """
        pass

    def get_properties(self):
        """
        获取所有非私有属性和由`@property`装饰器定义的属性。

        :return: 所有非私有属性和由`@property`装饰器定义的属性。
        :rtype: dict
        """
        return get_properties(self)

    def properties_to_dataframe(self):
        """
        将属性键值对转换为DataFrame。

        :return: 所有非私有属性和由`@property`装饰器定义的属性构建的DataFrame对象。
        :rtype: pandas.DataFrame
        """
        return create_df_from_dict(self.get_properties())


# ===========================================================
