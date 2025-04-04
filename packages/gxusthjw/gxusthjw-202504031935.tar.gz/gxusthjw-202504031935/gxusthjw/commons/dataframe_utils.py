#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        dataframe_utils.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 为`DataFrame相关操作`提供辅助方法和类。
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
import array
from collections import deque
from typing import Union, List, Tuple, Set

import numpy as np
import pandas as pd

# 声明 ==============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
Defining helper functions and classes for 
`operations related to DataFrame`.
"""

__all__ = [
    "ItemDataType",
    "create_df_from_item",
    "create_df_from_dict",
    "merge_dfs",
]


# 定义 ==============================================================

# 项数据类型。
ItemDataType = Union[
    List,  # list
    Tuple,  # tuple
    int,  # int
    float,  # float
    str,  # str
    bool,  # bool
    Set,  # set
    np.ndarray,  # NumPy ndarray
    pd.Series,  # Pandas Series
    array.array,  # array.array
    deque,  # collections.deque
]


def create_df_from_item(data: ItemDataType, name: str) -> pd.DataFrame:
    """
    从指定的数据和数据名创建pd.DataFrame。

    :param data: 指定的数据
    :param name: 指定的数据名。
    :return: 创建得到的DataFrame。
    """
    # 如果data不是可迭代的或者是一个字符串，将其转换为列表
    if not hasattr(data, "__iter__") or isinstance(data, str):
        data = [data]
    elif isinstance(data, (set, frozenset)):
        data = list(data)
    # 创建DataFrame
    return pd.DataFrame({name: data})


def create_df_from_dict(data: dict) -> pd.DataFrame:
    """
    从指定的字典创建pd.DataFrame。

    :param data: 指定的字典。
    :return: 创建得到的DataFrame。
    """
    # 将每个键值对转换为DataFrame，然后合并它们
    dfs = [create_df_from_item(v, k) for k, v in data.items()]
    # 使用pd.concat来合并所有的DataFrame
    return pd.concat(dfs, axis=1)


def merge_dfs(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    合并两个DataFrame，如果列名已存在，则覆盖df1中的列。

    :param df1: 第一个DataFrame。
    :param df2: 第二个DataFrame。
    :return: 合并后的DataFrame。
    :rtype: pandas.DataFrame
    """
    # 删除df1中与df2相同的列
    df1 = df1.drop(columns=df2.columns, errors="ignore")
    # 使用pd.concat合并两个DataFrame
    merged_df = pd.concat([df1, df2], axis=1)
    return merged_df
