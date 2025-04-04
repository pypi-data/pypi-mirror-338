#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        test_data_2d_region_sm_linear_fitter.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试data_2d_region_sm_linear_fitter.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2024/10/22     revise
# ------------------------------------------------------------------
# 导包 =============================================================
import unittest

import numpy as np
import statsmodels.api as sm
from .data_2d_region_sm_linear_fitter import Data2dRegionSmLinearFitter


# ==================================================================
class TestData2dRegionSmLinearFitter(unittest.TestCase):
    """
    测试data_2d_region_sm_linear_fitter.py。
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
        # 创建一些示例数据
        np.random.seed(0)  # 设置随机种子以便结果可复现
        x = np.arange(1000)  # 生成100个在[0,1)之间的随机数作为自变量
        y = 2 * x + 100 + np.random.randn(1000)  # 假设真实模型为 y = 2x + ε，ε是噪声
        # 将x转化为有常数项的形式，即添加一列全为1的列，代表截距项
        x_var = sm.add_constant(x)
        # 使用OLS方法拟合模型
        model = sm.OLS(y, x_var)
        results = model.fit()
        # 打印回归结果
        print(results.summary())
        # 获取回归系数
        beta_0, beta_1 = results.params
        print(f"截距项: {beta_0}, 斜率: {beta_1}")
        # ----------------------------------------------
        lf = Data2dRegionSmLinearFitter(y, x)
        lf.interactive_smooth()


if __name__ == '__main__':
    unittest.main()
