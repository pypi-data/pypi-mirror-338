#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        data_analyzer.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 定义“表征`数据分析器`”的类。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2024/09/30     revise
#       Jiwei Huang        0.0.1         2024/10/03     revise
#       Jiwei Huang        0.0.1         2024/10/09     revise
#       Jiwei Huang        0.0.1         2024/10/12     revise
#       Jiwei Huang        0.0.1         2024/10/16     revise
#       Jiwei Huang        0.0.1         2024/10/17     finish
# ------------------------------------------------------------------
# 导包 ============================================================
from .data_logger import DataLogger

# 声明 ============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
Defining a class that represents `Data Analyzer`.
"""

__all__ = [
    'DataAnalyzer'
]


# 定义 ============================================================
class DataAnalyzer(object):
    """
    类`DataAnalyzer`表征“数据分析器”。

    类`DataAnalyzer`是所有表征`数据分析器`的基类。此类拥有如下属性：

        1. data_analyzer_name：数据分析器的名称。

        2. data_logger: 数据记录器。
    """

    def __init__(self, *args, **kwargs):
        """
        类`DataAnalyzer`的初始化方法。

            消耗掉的可选关键字参数：

                1. data_analyzer_name：数据分析器的名称，默认值：DataAnalyzer。

                2. data_logger_owner: 数据记录器的归属，默认值：`self`

                3. data_logger_name：数据记录器的名称，默认值：`f"{数据分析器名称}_DataLogger"`。

        :param args: 可选参数。
        :param kwargs: 可选关键字参数。
        """
        self.__name = kwargs.pop('data_analyzer_name', self.__class__.__name__)
        data_logger_owner = kwargs.pop('data_logger_owner', self)
        data_logger_name = kwargs.pop('data_logger_name',
                                      f"{data_logger_owner.__class__.__name__}_DataLogger")
        # 初始化数据记录器。
        self.__data_logger = DataLogger(data_logger_owner, data_logger_name)
        self.__data_logger.log(self.__name, 'DataAnalyzerName')
        self.__data_logger.logs(*args, **kwargs)

        # 可选关键字参数将被转换为对象的属性。
        for key in kwargs.keys():
            if not hasattr(self, key):
                setattr(self, key, kwargs[key])

    @property
    def name(self):
        """
        返回数据分析器的名称。

        :return: 数据分析器的名称。
        :rtype: str
        """
        return self.__name

    @property
    def data_logger(self):
        """
        返回数据记录器。

        :return: 数据记录器。
        :rtype: DataLogger
        """
        return self.__data_logger
# ===============================================================
