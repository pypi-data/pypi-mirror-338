#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        typings.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 定义"类型标注"相关的类和函数。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/30     revise
#       Jiwei Huang        0.0.1         2024/08/20     revise
#       Jiwei Huang        0.0.1         2024/10/08     revise
#       Jiwei Huang        0.0.1         2024/10/13     revise
# ------------------------------------------------------------------
# 导包 =============================================================
import numbers
from typing import Union, TypeVar, List, Tuple
from collections.abc import Iterable, Sequence

import numpy as np
import numpy.typing as npt

# 声明 =============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
Defining functions and classes for `typing (type annotations)`.
"""

__all__ = [
    'Number',
    'is_number',
    'NumberArrayLike',
    'is_number_array_like',
    'NumberSequence',
    'is_number_sequence',
    'Numbers',
    'is_numbers',
    'Numeric',
    'is_numeric',
]

# 定义 ===============================================================
Number = TypeVar('Number', int, float)
"""
数值。
"""


def is_number(value: Number) -> bool:
    """
    判断指定值是否为数值。

    :param value: 要判断的值。
    :return: 如果指定的值是数值，返回True，否则返回False。
    """
    return isinstance(value, (int, float))


NumberArrayLike = Union[
    List[Union[int, float]],
    Tuple[Union[int, float], ...],
    npt.NDArray[np.number]
]
"""
数值型类数组。
"""


def is_number_array_like(data) -> bool:
    """
    检查给定的数据是否为 NumberArrayLike 类型。

    :param data: 要检查的数据。
    :return: 如果数据是 NumberArrayLike 类型则返回 True，
    否则返回 False。
    """
    if isinstance(data, (list, tuple)):
        # 检查列表或元组中的所有元素是否都是 int 或 float
        return all(isinstance(item, (int, float)) for item in data)
    elif isinstance(data, np.ndarray):
        # 检查 NumPy 数组是否只包含数值类型的元素
        return issubclass(data.dtype.type, np.number)
    else:
        # 数据既不是 list/tuple 也不是 np.ndarray
        return False


NumberSequence = Union[
    Sequence[Number],
    npt.NDArray[np.number]
]
"""
数值型序列。
"""


def is_number_sequence(data) -> bool:
    """
    检查给定的数据是否为 NumberSeq 类型。

    :param data: 要检查的数据。
    :return: 如果数据是 NumberSeq 类型则返回 True，否则返回 False。
    """
    if isinstance(data, np.ndarray):
        return issubclass(data.dtype.type, np.number)
    if isinstance(data, Sequence):
        length = len(data)
        for i in range(length):
            if not isinstance(data[i], (int, float)):
                return False
        return True
    else:
        return False


Numbers = Union[
    Iterable[Number],
    npt.NDArray[np.number]
]
"""
数值集。
"""


def is_numbers(data) -> bool:
    """
    检查给定的数据是否为 Numbers 类型。

    :param data: 要检查的数据。
    :return: 如果数据是 Numbers 类型则返回 True，否则返回 False。
    """
    if isinstance(data, np.ndarray):
        # 检查 NumPy 数组是否只包含数值类型的元素
        return issubclass(data.dtype.type, np.number)
    elif hasattr(data, '__iter__'):
        # 检查可迭代对象中的所有元素是否都是数字
        try:
            return all(isinstance(item, numbers.Number) for item in data)
        except TypeError:
            # 如果迭代过程中出现类型错误，则认为不符合条件
            return False
    else:
        # 数据既不是 np.ndarray 也不是可迭代对象
        return False


Numeric = TypeVar('Numeric', int, float, npt.NDArray[np.number])
"""
数值。
"""


def is_numeric(data) -> bool:
    """
    检查给定的数据是否为 Numeric 类型。

    :param data: 要检查的数据。
    :return: 如果数据是 Numeric 类型则返回 True，否则返回 False。
    """
    if isinstance(data, (int, float)):
        return True
    elif isinstance(data, np.ndarray):
        # 检查 NumPy 数组是否只包含数值类型的元素
        return issubclass(data.dtype.type, np.number)
    else:
        return False
