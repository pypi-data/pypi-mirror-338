#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        test_array_utils.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试array_utils.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/30     revise
#       Jiwei Huang        0.0.1         2024/06/11     revise
#       Jiwei Huang        0.0.1         2024/07/31     revise
#       Jiwei Huang        0.0.1         2024/08/20     revise
# ------------------------------------------------------------------
# 导包 =============================================================
import unittest
import numpy as np
from .array_utils import (is_sorted,
                          is_sorted_ascending,
                          is_sorted_descending,
                          reverse, Ordering,
                          is_equals_of,
                          sort,
                          find_closest_index,
                          find_crossing_index)


# ==================================================================

class TestArrayUtils(unittest.TestCase):
    """
    测试array_utils.py。
    """

    # ==============================================================
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

    # ==============================================================

    def test_is_sorted(self):
        x1 = [1, 2, 3, 4, 5, 6, 8, 10, 110]
        self.assertEqual(True, is_sorted(x1))
        self.assertEqual(True, is_sorted_ascending(x1))
        self.assertEqual(False, is_sorted_descending(x1))

        x1_r = reverse(x1)
        self.assertEqual(True, is_sorted(x1_r))
        self.assertEqual(False, is_sorted_ascending(x1_r))
        self.assertEqual(True, is_sorted_descending(x1_r))
        print()
        print(x1_r)

    def test_ordering(self):
        print(Ordering['UNORDERED'])
        print(Ordering['UNORDERED'].value)
        print(Ordering['ASCENDING'].value)
        print(Ordering['ASCENDING'])
        print(Ordering['DESCENDING'].value)
        print(Ordering['DESCENDING'])

    def test_is_equals_of(self):
        a = [1.0, 2.0, 3.0, 4.0]
        self.assertTrue(is_equals_of(a, a))

    def test_sort(self):
        x1 = [1, 2, 3, 4, 5, 6, 8, 10, 110]
        print(x1)
        print(sort(x1, ordering=Ordering.DESCENDING))
        self.assertTrue(is_equals_of(np.array([110, 10, 8, 6, 5, 4, 3, 2, 1]),
                                     sort(x1, ordering=Ordering.DESCENDING)))
        self.assertTrue(np.allclose(np.array([110, 10, 8, 6, 5, 4, 3, 2, 1]),
                                    sort(x1, ordering=Ordering.DESCENDING)))
        x1 = [1, 2, -3, 4, 5, -6, 8, 10, -110]
        print(x1)
        print(sort(x1, ordering=Ordering.DESCENDING))
        self.assertTrue(is_equals_of(np.array([10, 8, 5, 4, 2, 1, -3, -6, -110]),
                                     sort(x1, ordering=Ordering.DESCENDING)))
        x1 = [-1, -2, -3, -4, -5, -6, -8, -10, -110]
        print(x1)
        print(sort(x1, ordering=Ordering.DESCENDING))
        self.assertTrue(is_equals_of(np.array([-1, -2, -3, -4, -5, -6, -8, -10, -110]),
                                     sort(x1, ordering=Ordering.DESCENDING)))

    def test_find_closest_index(self):
        arr_asc = np.array([1, 3, 5, 7, 9, 11])  # 升序数组
        arr_desc = np.array([11, 9, 7, 5, 3, 1])  # 降序数组
        value_to_find = 6  # 假设我们要找的值是 6

        index_asc = find_closest_index(arr_asc, value_to_find)
        index_desc = find_closest_index(arr_desc, value_to_find)

        print(f"The index of the closest value to {value_to_find} in ascending array is {index_asc}.")
        print(f"The index of the closest value to {value_to_find} in descending array is {index_desc}.")

    def test_find_crossing_index(self):
        a = np.array([1, 2, 4, 5])
        v = 3
        index = np.searchsorted(a, v)
        print(index)  # 输出 2
        arr_asc = np.array([1, 3, 5, 7, 9, 11])  # 升序数组
        arr_desc = np.array([11, 9, 7, 5, 3, 1])  # 降序数组
        value_to_find = 6  # 假设我们要找的值是 6

        index_asc = find_crossing_index(arr_asc, value_to_find)
        index_desc = find_crossing_index(arr_desc, value_to_find)

        print(f"The index of the closest value to {value_to_find} in ascending array is {index_asc}.")
        print(f"The index of the closest value to {value_to_find} in descending array is {index_desc}.")


if __name__ == '__main__':
    unittest.main()
