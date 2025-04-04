#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        test_data_2d.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试data_2d.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2024/09/15     revise
#       Jiwei Huang        0.0.1         2024/09/18     revise
#       Jiwei Huang        0.0.1         2024/09/28     revise
#       Jiwei Huang        0.0.1         2024/10/14     revise
#       Jiwei Huang        0.0.1         2024/10/20     revise
#       Jiwei Huang        0.0.1         2024/10/22     finish
# ------------------------------------------------------------------
# 导包 =============================================================
import unittest

import numpy as np

from .data_2d import Data2d


# ==================================================================
class TestData2d(unittest.TestCase):
    """
    测试data_2d.py。
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
        d = Data2d([1])
        self.assertTrue(np.array_equal(d.data_y, np.array([1])))
        self.assertTrue(np.array_equal(d.data_x, np.array([0])))
        self.assertEqual(1, d.data_len)
        self.assertEqual(1, d.data_x_len)
        self.assertEqual(1, d.data_y_len)

        da = Data2d([1, 2])
        self.assertTrue(np.array_equal(da.data_y, np.array([1, 2])))
        self.assertTrue(np.array_equal(da.data_x, np.array([0, 1])))
        self.assertEqual(2, da.data_len)
        self.assertEqual(2, da.data_x_len)
        self.assertEqual(2, da.data_y_len)

        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        d1 = Data2d(y)
        self.assertTrue(np.allclose(d1.data_y, np.asarray(y)))
        self.assertTrue(np.allclose(d1.data_x, np.arange(11)))
        self.assertEqual(d1.data_len, 11)
        self.assertEqual(d1.data_x_len, 11)
        self.assertEqual(d1.data_y_len, 11)
        self.assertTrue(d1.is_aligned)
        print(d1.data)
        print(d1.exog)
        print(d1.endog)

        d2 = Data2d(y, x)
        self.assertTrue(np.allclose(d2.data_y, np.asarray(y)))
        self.assertTrue(np.allclose(d2.data_x, np.asarray(x)))
        self.assertEqual(d2.data_len, 10)
        self.assertEqual(d2.data_x_len, 10)
        self.assertEqual(d2.data_y_len, 11)
        self.assertFalse(d2.is_aligned)
        print(d2.data)
        print(d2.exog)
        print(d2.endog)

        d3 = Data2d([])
        print(d3.data_y)

    def test_iter(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        d2 = Data2d(y, x)
        for xi, yi in d2:
            print(xi, yi)

    def test_str(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        d1 = Data2d(y, x)
        self.assertEqual(d1.__len__(), 11)
        print(d1.__str__())
        print(d1.__repr__())
        d2 = eval(repr(d1))
        print(d2)

        d3 = eval(str(d1))
        print(d3)
        print(d2.data)
        print(d2.get_x(5))
        print(d2.get_y(5))
        print(d2.get_xy(5))

    def test_view(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        d1 = Data2d(y, x)
        d1.view()
        d1.view(label='A')

    def test_span_select(self):
        np.random.seed(19680801)
        x = np.arange(0.0, 5.0, 0.01)
        y = np.sin(2 * np.pi * x) + 0.5 * np.random.randn(len(x))
        d1 = Data2d(y, x)
        new_y, new_x = d1.span_select()
        new_d = Data2d(new_y, new_x)
        new_d.view(label='New')
        new_d2 = Data2d(*d1.span_select())
        new_d2.view(label='New')


if __name__ == '__main__':
    unittest.main()
