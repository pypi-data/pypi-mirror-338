#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        test_raw400_file.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试raw400_file.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2024/09/24     revise
# ------------------------------------------------------------------
# 导包 =============================================================
import os
import unittest

from .raw400_file import XrdRaw400File, XrdRaw400Folder


# ==================================================================
class TestRaw400File(unittest.TestCase):
    """
    测试raw400_file.py。
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
    # noinspection PyUnresolvedReferences
    def test_xrdraw400file(self):
        # --------------------------------------------------------
        this_file = __file__
        print("this file: %s" % this_file)
        this_file_path, this_file_name = os.path.split(this_file)
        print('this file name: %s' % this_file_name)
        print('this_file_path: %s' % this_file_path)
        # --------------------------------------------------------
        data_file_path = os.path.join(this_file_path, 'test_data', 'raw400_file')
        data_file_name = '0.4-0.4-no salt-ethanol treatment.txt'
        data_file = os.path.join(data_file_path, data_file_name)
        print("===============================================")
        print("data file: %s" % data_file)
        print("===============================================")
        # -------------------------------------------------------
        raw_file = XrdRaw400File(data_file)
        print(raw_file.data)

    def test_xrdraw400folder(self):
        # --------------------------------------------------------
        this_file = __file__
        print("this file: %s" % this_file)
        this_file_path, this_file_name = os.path.split(this_file)
        print('this file name: %s' % this_file_name)
        print('this_file_path: %s' % this_file_path)
        # --------------------------------------------------------
        data_file_path = os.path.join(this_file_path, 'test_data', 'raw400_file')
        print("===============================================")
        print("data_file_path: %s" % data_file_path)
        print("===============================================")
        # -------------------------------------------------------
        out_file = os.path.join(os.path.join(this_file_path, 'test_out', 'raw400_file'), 'merge_all.csv')
        raw_folder = XrdRaw400Folder(data_file_path)
        raw_folder.to_csv(out_file)


if __name__ == '__main__':
    unittest.main()
