#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        test_typings.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试typings.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2024/10/13     revise
# ------------------------------------------------------------------
# 导包 =============================================================
import unittest

import numpy as np

from .typings import (is_number,
                      is_number_array_like,
                      is_number_sequence,
                      is_numbers,
                      is_numeric)


# ==================================================================
class TestTypings(unittest.TestCase):
    """
    测试typings.py。
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

    # noinspection PyTypeChecker
    def test_is_number(self):
        self.assertTrue(is_number(1))
        self.assertTrue(is_number(1.0))
        self.assertFalse(is_number('1'))
        self.assertFalse(is_number("1"))
        self.assertFalse(is_number(object))

    def test_is_number_array_like(self):
        self.assertTrue(is_number_array_like([]))
        self.assertTrue(is_number_array_like(tuple()))
        self.assertTrue(is_number_array_like([1, 2, 3]))
        self.assertTrue(is_number_array_like((1, 2, 3)))
        test_data = [
            [1, 2.5, 3],  # 列表，符合条件
            (4, 5.6, 7),  # 元组，符合条件
            np.array([8, 9.0]),  # NumPy 数组，符合条件
            [1, 'two', 3],  # 包含非数字的列表
            ('four', 5.0),  # 包含非数字的元组
            np.array(['six', 7]),  # 包含非数字的 NumPy 数组
            "not a number",  # 字符串，不符合条件
            42  # 单个数字，但不是列表/元组/数组
        ]

        for td in test_data:
            print(f"Data: {td} is NumberArrayLike? {is_number_array_like(td)}")

    def test_is_number_seq(self):
        test_data = [
            [1, 2.5, 3],  # 列表，符合条件
            (4, 5.6, 7),  # 元组，符合条件
            np.array([8, 9.0]),  # NumPy 数组，符合条件
            [1, 'two', 3],  # 包含非数字的列表
            ('four', 5.0),  # 包含非数字的元组
            np.array(['six', 7]),  # 包含非数字的 NumPy 数组
            "not a number",  # 字符串，不符合条件
            42,  # 单个数字，但不是序列或数组
            {1, 2, 3, 4, 5}
        ]

        for td in test_data:
            print(f"Data: {td} is NumberSeq? {is_number_sequence(td)}")

    def test_is_numbers(self):
        test_data = [
            [1, 2.5, 3],  # 列表，符合条件
            (4, 5.6, 7),  # 元组，符合条件
            np.array([8, 9.0]),  # NumPy 数组，符合条件
            {1, 2.5, 3},  # 集合，符合条件
            range(5),  # range 对象，符合条件
            [1, 'two', 3],  # 包含非数字的列表
            ('four', 5.0),  # 包含非数字的元组
            np.array(['six', 7]),  # 包含非数字的 NumPy 数组
            "not a number",  # 字符串，不符合条件
            42,  # 单个数字，但不是可迭代对象
            {1, 2, 3, 4, 5}
        ]

        for td in test_data:
            print(f"Data: {td} is Numbers? {is_numbers(td)}")

    def test_is_numeric(self):
        test_data = [
            1,  # 整数，符合条件
            2.5,  # 浮点数，符合条件
            np.array([8, 9.0]),  # NumPy 数组，符合条件
            [1, 2, 3],  # 列表，不符合条件
            'not a number',  # 字符串，不符合条件
            42.0 + 3j,  # 复数，不符合条件
            (4, 5.6),  # 元组，不符合条件
            {'key': 42},  # 字典，不符合条件
        ]

        for td in test_data:
            print(f"Data: {td} is Numeric? {is_numeric(td)}")


if __name__ == '__main__':
    unittest.main()
