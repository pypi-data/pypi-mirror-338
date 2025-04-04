#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        array_utils.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 为`类似数组`的对象提供辅助方法和类。
#                   Outer Parameters: xxxxxxx
# Class List:       Ordering -- 枚举`Ordering`表征有序性。
# Function List:    is_sorted(arr) --
#                                              判断指定的值组是否为有序的。
#                   is_sorted_ascending(arr) --
#                                              判断指定的值组是否为升序的。
#                   is_sorted_descending(arr) --
#                                              判断指定的值组是否为降序的。
#                   reverse(arr) -- 将指定的值组倒置。
#                   is_equals_of(arr1,arr2,rtol=0, atol=1e-9) --
#                                              判断两个数组的相等性。
#                   sort(arr,ordering) -- 获取给定数值组的有序copy。
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/30     revise
#       Jiwei Huang        0.0.1         2024/06/11     revise
#       Jiwei Huang        0.0.1         2024/07/31     revise
#       Jiwei Huang        0.0.1         2024/08/20     revise
# ------------------------------------------------------------------
# 导包 =============================================================
from typing import Union
from enum import Enum
import numpy as np
import numpy.typing as npt

from .typings import NumberArrayLike, Number

# 声明 ============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
Defining helper functions and classes for `array-like` objects.
"""

__all__ = [
    "is_sorted",
    "is_sorted_ascending",
    "is_sorted_descending",
    "reverse",
    "is_equals_of",
    "Ordering",
    "sort",
    "find_closest_index",
    "find_crossing_index",
    "find_index_range",
]


# 定义 =================================================================
def is_sorted(arr: NumberArrayLike) -> bool:
    """
    判断给定的数值组是否为有序排列（升序或降序）。

    如果给定的数值组是有序的，则返回 True；否则返回 False。

    :param arr: 给定的数值组。
    :return: 如果给定的数值组是有序的，则返回 True；否则返回 False。
    """
    value_arr = np.asarray(arr)
    return np.all(np.diff(value_arr) >= 0) or np.all(np.diff(value_arr) <= 0)


def is_sorted_ascending(arr: NumberArrayLike) -> bool:
    """
    判断给定的数值组是否为升序的。

    如果给定的数值组是是升序的，返回True，否则返回False。

    :param arr: 给定的数值组。
    :return:如果给定的数值组是是升序的，返回True，否则返回False。
    """
    value_arr = np.asarray(arr)
    return np.all(np.diff(value_arr) >= 0)


def is_sorted_descending(arr: NumberArrayLike) -> bool:
    """
    判断给定的数值组是否为降序的。

    如果给定的数值组是是降序的，返回True，否则返回False。

    :param arr: 给定的数值组。
    :return:如果给定的数值组是是降序的，返回True，否则返回False。
    """
    value_arr = np.asarray(arr)
    return np.all(np.diff(value_arr) <= 0)


def reverse(arr: NumberArrayLike) -> npt.NDArray[np.number]:
    """
    将给定的数值组倒置。

    :param arr: 给定的数值组。
    :return: 倒置后的数值组。
    """
    value_arr = np.asarray(arr)
    return np.array(value_arr[::-1], copy=True)


def is_equals_of(
    arr1: NumberArrayLike, arr2: NumberArrayLike, rtol=0, atol=1e-9
) -> bool:
    """
    判断给定的两个数值组的相等性。

    第1个参数记为：a

    第2个参数记为：b

    则下式为True，此函数返回True：

        absolute(a - b) <= (atol + rtol * absolute(b))

    :param arr1: 数值组1。
    :param arr2: 数值组2。
    :param rtol: 相对容差，相对容差是指：两个数之差除以第2个数。
    :param atol: 绝对容差，绝对容差是指：两个数之差。
    :return:如果给定的两个数值组相等，则返回True，否则返回false。
    """
    return np.allclose(
        np.asarray(arr1), np.asarray(arr2), rtol=rtol, atol=atol, equal_nan=True
    )


class Ordering(Enum):
    """
    枚举`Ordering`表征有序性。
    """

    # 无序。
    UNORDERED = 0
    """
    ‘UNORDERED’表征`无序`。
    """

    # 升序。
    ASCENDING = 1
    """
    ‘ASCENDING’表征`升序`。
    """

    # 降序。
    DESCENDING = 2
    """
    ‘DESCENDING’表征`降序`。
    """

    # noinspection DuplicatedCode
    @staticmethod
    def of(value: Union[int, str]):
        """
        从值或成员名（忽略大小写）构建枚举实例。

        :param value: 指定的值或成员名（忽略大小写）。
        :return: Ordering对象。
        :rtype: Ordering
        """
        if isinstance(value, str):
            if value.upper() in Ordering.__members__:
                return Ordering.__members__[value]
            else:
                raise ValueError(f"Unknown value ({value}) for Ordering.")
        elif isinstance(value, int):
            for member in Ordering:
                if member.value == value:
                    return member
            raise ValueError(f"Unknown value ({value}) for Ordering.")
        else:
            raise ValueError(f"Unknown value ({value}) for Ordering.")


def sort(
    arr: NumberArrayLike, ordering: Ordering = Ordering.ASCENDING
) -> npt.NDArray[np.number]:
    """
    获取给定数值组的有序copy。

    :param arr: 给定的数值组。
    :param ordering: 指定升序或降序。
    :return: 有序的数值组。
    """
    arr_sorted = np.sort(arr)
    if ordering == Ordering.DESCENDING:
        return reverse(arr_sorted)
    return arr_sorted


def find_closest_index(ordered_arr: NumberArrayLike, value: Number):
    """
    在指定有序数组中找到最接近指定值的索引。

    此方法与find_crossing_index方法的目标是一致的，但两者的算法并不相同。

    降序与升序的结果不同。

    :param ordered_arr: 指定的有序数组。
    :param value: 指定的值。
    :return: 指定有序数组中找到最接近指定值的索引。
    """
    ordered_arr = np.asarray(ordered_arr)
    if is_sorted_ascending(ordered_arr):
        if not (ordered_arr[0] <= value <= ordered_arr[-1]):
            return None
        # 对于升序数组
        idx = np.searchsorted(ordered_arr, value)
        if idx < len(ordered_arr) and ordered_arr[idx] == value:
            return idx
        if idx == 0:
            return 0
        elif idx == len(ordered_arr):
            return len(ordered_arr) - 1
        else:
            before = ordered_arr[idx - 1]
            after = ordered_arr[idx]
            if after - value < value - before:
                return idx
            else:
                return idx - 1
    elif is_sorted_descending(ordered_arr):
        if not (ordered_arr[-1] <= value <= ordered_arr[0]):
            return None
        # 对于降序数组
        reversed_arr = ordered_arr[::-1]
        rev_idx = np.searchsorted(reversed_arr, value)
        if rev_idx < len(reversed_arr) and reversed_arr[rev_idx] == value:
            return len(ordered_arr) - 1 - rev_idx
        if rev_idx == 0:
            return len(ordered_arr) - 1
        elif rev_idx == len(reversed_arr):
            return 0
        else:
            before = reversed_arr[rev_idx - 1]
            after = reversed_arr[rev_idx]
            if after - value < value - before:
                return len(ordered_arr) - 1 - rev_idx
            else:
                return len(ordered_arr) - 1 - (rev_idx - 1)
    else:
        raise ValueError("Expected arr is ordered.")


def find_crossing_index(ordered_arr: NumberArrayLike, value: Number):
    """
    在指定有序数组中找到最接近指定值的索引。

    此方法与find_closest_index方法的目标是一致的，但两者的算法并不相同。

    无论是降序或升序，其结果均相同。

    :param ordered_arr: 指定的有序数组。
    :param value: 指定的值。
    :return: 指定有序数组中找到最接近指定值的索引。
    """
    if not is_sorted(ordered_arr):
        raise ValueError("Expected arr is ordered.")
    ordered_arr = np.asarray(ordered_arr)
    if (ordered_arr[0] <= value <= ordered_arr[-1]) or (
        ordered_arr[-1] <= value <= ordered_arr[0]
    ):
        # 找到符号变化的位置
        sign_changes = np.where(np.diff(np.sign(ordered_arr - value)) != 0)[0]
        # 计算交叉点的索引
        cross_indices = sign_changes + (value - ordered_arr[sign_changes]) / (
            ordered_arr[sign_changes + 1] - ordered_arr[sign_changes]
        )
        # 添加等于 strain_value 的位置
        equal_indices = np.where(ordered_arr == value)[0]
        # 合并索引并排序
        all_indices = np.sort(np.concatenate((cross_indices, equal_indices)))
        # 返回最接近的索引
        return int(np.round(all_indices[0])) if all_indices.size > 0 else None
    else:
        return None


def find_index_range(ordered_arr: NumberArrayLike, value1: Number, value2: Number):
    """
    获取两个指定值范围的索引范围。

    :param ordered_arr: 指定的有序数组。
    :param value1: 指定的值1。
    :param value2: 指定的值2。
    :return: 两个指定值范围的索引范围。
    """
    value1_index = find_crossing_index(ordered_arr, value1)
    value2_index = find_crossing_index(ordered_arr, value2)
    return (
        (value1_index, value2_index)
        if value2_index > value1_index
        else (value2_index, value1_index)
    )
