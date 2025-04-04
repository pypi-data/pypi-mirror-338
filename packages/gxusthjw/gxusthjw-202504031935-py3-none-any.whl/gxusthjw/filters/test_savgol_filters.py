#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        test_savgol_filters.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试savgol_filters.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2024/09/01     revise
#       Jiwei Huang        0.0.1         2024/09/03     revise
#       Jiwei Huang        0.0.1         2024/10/19     revise
#       Jiwei Huang        0.0.1         2024/10/20     finish
# ------------------------------------------------------------------
# 导包 =============================================================
import unittest

import numpy as np

from .savgol_filters import (simple_interactive_savgol_filter,
                             all_interactive_savgol_filter,
                             interactive_savgol_filter,
                             static_savgol_filter, )


# ==================================================================
class TestSavgolFilters(unittest.TestCase):
    """
    测试savgol_filters.py。
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
    def test_simple_interactive_savgol_filter(self):
        # 创建一些测试数据 ---------------------------------
        np.random.seed(0)
        x = np.linspace(0, 10 * np.pi, 1000)
        y = np.sin(x) + 0.5 * np.random.normal(size=x.shape)
        # ------------------------------------------------
        res = simple_interactive_savgol_filter(y, x)
        print(res[0])
        print("--------------------------------")
        print(res[1])
        print("--------------------------------")
        print(res[2])

    def test_all_interactive_savgol_filter(self):
        # 创建一些测试数据 ---------------------------------
        np.random.seed(0)
        x = np.linspace(0, 10 * np.pi, 1000)
        y = np.sin(x) + 0.5 * np.random.normal(size=x.shape)
        # ------------------------------------------------
        res = all_interactive_savgol_filter(y, x)
        print(res[0])
        print("--------------------------------")
        print(res[1])
        print("--------------------------------")
        print(res[2])

    def test_interactive_savgol_filter(self):
        # 创建一些测试数据 ---------------------------------
        np.random.seed(0)
        x = np.linspace(0, 10 * np.pi, 1000)
        y = np.sin(x) + 0.5 * np.random.normal(size=x.shape)
        # ------------------------------------------------
        res = interactive_savgol_filter(y, x, interactive_mode='simple')
        print(res[0])
        print("--------------------------------")
        print(res[1])
        print("--------------------------------")
        print(res[2])

    def test_interactive_savgol_filter2(self):
        # 创建一些测试数据 ---------------------------------
        np.random.seed(0)
        x = np.linspace(0, 10 * np.pi, 1000)
        y = np.sin(x) + 0.5 * np.random.normal(size=x.shape)
        # ------------------------------------------------
        res = interactive_savgol_filter(y, x, interactive_mode='all')
        print(res[0])
        print("--------------------------------")
        print(res[1])
        print("--------------------------------")
        print(res[2])

    def test_static_savgol_filter(self):
        # 创建一些测试数据 ---------------------------------
        np.random.seed(0)
        x = np.linspace(0, 10 * np.pi, 1000)
        y = np.sin(x) + 0.5 * np.random.normal(size=x.shape)
        # ------------------------------------------------
        static_savgol_filter(y, x, is_plot=True, is_show_fig=True)


if __name__ == '__main__':
    unittest.main()
