#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        test_data_analyzer.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试data_analyzer.py。
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
# 导包 =============================================================
import unittest

from .data_analyzer import DataAnalyzer


# ==================================================================
class TestDataAnalyzer(unittest.TestCase):
    """
    测试data_analyzer.py。
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
        da = DataAnalyzer()
        print(da.name)
        da.data_logger.print()

        da = DataAnalyzer(1, (1,), [1, 2], {'a': 1, 'b': 2})
        print(da.name)
        da.data_logger.print()

        da = DataAnalyzer(1, (1,), [1, 2], {'a': 1, 'b': 2},
                          data_analyzer_name="data_analyzer_name",
                          data_logger_name="data_logger_name")
        print(da.name)
        da.data_logger.print()

        da = DataAnalyzer(1, (1,), [1, 2], {'a': 1, 'b': 2},
                          data_analyzer_name="data_analyzer_name",
                          data_logger_name="data_logger_name",
                          c=1, b=3, d=4)

        print(da.name)
        da.data_logger.print()


if __name__ == '__main__':
    unittest.main()
