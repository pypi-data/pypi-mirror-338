#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        test_sm_linear_fitters.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试sm_linear_fitters.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2024/10/18     revise
#       Jiwei Huang        0.0.1         2024/10/22     finish
# ------------------------------------------------------------------
# 导包 =============================================================
import os
import unittest

import numpy as np
import statsmodels.api as sm
from .sm_linear_fitters import (static_linear_fitting_sm,
                                interactive_linear_fitting_sm)


# ==================================================================
class TestSmLinearFitters(unittest.TestCase):
    """
    测试sm_linear_fitters.py。
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

    def test_static_linear_fitting_sm(self):
        # 示例数据
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

        # 调用 static_linear_fitting_sm 函数
        var_y_fitted, y_var, x_var, fitting_result = static_linear_fitting_sm(
            y, x,
            region_start=0,
            region_length=10,
            method="ols",
            view_start=0,
            view_length=6,
            is_data_out=True,
            data_outfile_name="static_linear_fitting_ols",
            data_outpath="./test_out",
            is_print_summary=True,
            is_plot=True,
            is_fig_out=True,
            fig_outfile_name="static_linear_fitting_ols",
            fig_outpath="./test_out",
            is_show_fig=True,
            title="OLS Linear Fitting",
            figsize=(15, 8),
            s=5,
            marker='o'
        )

        # 输出拟合结果
        print("拟合结果:")
        print(f"参数估计: {fitting_result.params}")
        print(f"标准误差: {fitting_result.bse}")
        print(f"R-squared: {fitting_result.rsquared}")
        print(f"调整后的 R-squared: {fitting_result.rsquared_adj}")
        print(f"残差标准误 (MSE): {fitting_result.mse_resid}")
        print(f"F 统计量: {fitting_result.fvalue}")
        print(f"p 值: {fitting_result.f_pvalue}")

        # 预测新数据点
        x_new = np.array([11, 12, 13])
        x_new_with_const = sm.add_constant(x_new)
        y_pred = fitting_result.predict(x_new_with_const)

        print("\n预测结果:")
        print(f"新数据点: {x_new}")
        print(f"预测值: {y_pred}")

    def test_interactive_linear_fitting_sm(self):
        # 生成示例数据
        np.random.seed(0)
        x = np.linspace(0, 10, 100)
        y = 2 * x + 1 + np.random.normal(0, 2, size=x.shape)

        method = 'ols'
        save_path = "./fitters/test_out"
        save_path = os.path.abspath(save_path)
        if not os.path.exists(save_path):
            os.makedirs(save_path, exist_ok=True)

        # 调用 interactive_linear_fitting_sm 函数
        var_y_fitted, var_y, var_x, fitting_result = interactive_linear_fitting_sm(
            y, x,
            title="Interactive Linear Fitting",
            figsize=(15, 8),
            s=5,
            marker='o',
            region_start=0,
            region_length=50,
            method=method,
            view_start=0,
            view_length=50,
            save_path=save_path
        )
        if method.strip().lower() == 'ols':
            # 打印拟合结果
            print("拟合结果:")
            print(f"参数估计: {fitting_result.params}")
            print(f"标准误差: {fitting_result.bse}")
            print(f"R-squared: {fitting_result.rsquared}")
            print(f"调整后的 R-squared: {fitting_result.rsquared_adj}")
            print(f"残差标准误 (MSE): {fitting_result.mse_resid}")
            print(f"F 统计量: {fitting_result.fvalue}")
            print(f"p 值: {fitting_result.f_pvalue}")
        else:
            print("拟合结果:")
            print(f"参数估计: {fitting_result.params}")
            print(f"标准误差: {fitting_result.bse}")
            print(f"残差自由度 (df_resid): {fitting_result.df_resid}")
            print(f"尺度参数 (Scale): {fitting_result.scale}")

        # 预测新数据点
        x_new = np.array([11, 12, 13])
        # noinspection PyPep8Naming
        X_new = sm.add_constant(x_new)
        y_pred = fitting_result.predict(X_new)

        print("\n预测结果:")
        print(f"新数据点: {x_new}")
        print(f"预测值: {y_pred}")


if __name__ == '__main__':
    unittest.main()
