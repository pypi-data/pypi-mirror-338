#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        test_logger_object.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试logger_object.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2024/11/11     revise
# ------------------------------------------------------------------
# 导包 =============================================================
import unittest

import pandas as pd

# noinspection PyProtectedMember
from .logger_object import LoggerObject, get_properties0


# ==================================================================
class LoggerObjectImpl(LoggerObject):
    def __init__(self, name, id, **kwargs):
        self.__name = name
        self.__id = id
        self._email = "huangjiwei@gxust.edu.cn"

        # 其他关键字参数被转换为对象的属性。
        for key in kwargs.keys():
            if not hasattr(self, key):
                setattr(self, key, kwargs[key])

    @property
    def name(self):
        """
        返回对象的名称。
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def id(self):
        """
        返回对象的编号。
        """
        return self.__id

    @property
    def email(self):
        """
        返回对象的电子邮件地址。
        """
        return self._email

    @property
    def idenfier(self):
        """
        返回对象的标识符。
        """
        return "{}-{}".format(self.__name, self.__id)

    def set_property(self, key, value):
        setattr(self, key, value)

    def a_method(self, dd):
        return self.idenfier + "a_method" + dd

    def _b_method(self, dd):
        return self.idenfier + "b_method" + dd


class TestLoggerObject(unittest.TestCase):
    """
    测试logger_object.py。
    """

    # --------------------------------------------------------------------
    def setUp(self):
        """
        Hook method for setting up the test fixture before exercising it.
        """
        print("\n\n-----------------------------------------------------")

    def tearDown(self):
        """
        Hook method for deconstructing the test fixture after testing it.
        """
        print("-----------------------------------------------------")

    @classmethod
    def setUpClass(cls):
        """
        Hook method for setting up class fixture before running tests in the class.
        """
        print("\n\n=======================================================")

    @classmethod
    def tearDownClass(cls):
        """
        Hook method for deconstructing the class fixture after running all tests in the class.
        """
        print("=======================================================")

    # --------------------------------------------------------------------

    def test_init(self):
        loi = LoggerObjectImpl("jiwei", 0)
        print(loi.properties_to_dataframe())
        print(get_properties0(loi))
        loi.set_property("a", 1)
        loi.set_property("b", pd.Series([1]))
        loi.set_property("c", pd.Series([1, 1, 2, 3]))
        loi.set_property("d", pd.Series([]))
        loi.set_property("e", None)
        print(loi.properties_to_dataframe())
        # print(get_properties0(loi))


if __name__ == "__main__":
    unittest.main()
