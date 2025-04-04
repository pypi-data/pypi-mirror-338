#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        data_2d_region_savgol_filters.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试data_2d_region_savgol_filters.py。
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

from .data_2d_region_savgol_filters import Data2dRegionSavgolFilter


# ==================================================================
class TestData2dRegionSavgolFilters(unittest.TestCase):
    """
    测试data_2d_region_savgol_filters.py。
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

    def test_simple_interactive_smooth(self):

        # 创建一些测试数据 ---------------------------------
        np.random.seed(0)
        x = np.linspace(0, 10 * np.pi, 1000)
        y = np.sin(x) + 0.5 * np.random.normal(size=x.shape)
        # ------------------------------------------------
        drsf = Data2dRegionSavgolFilter(y, x)
        drsf.interactive_smooth()

    def test_all_interactive_smooth(self):

        # 创建一些测试数据 ---------------------------------
        np.random.seed(0)
        x = np.linspace(0, 10 * np.pi, 1000)
        y = np.sin(x) + 0.5 * np.random.normal(size=x.shape)
        # ------------------------------------------------
        drsf = Data2dRegionSavgolFilter(y, x)
        drsf.interactive_smooth(interactive_mode="all")


if __name__ == "__main__":
    unittest.main()
