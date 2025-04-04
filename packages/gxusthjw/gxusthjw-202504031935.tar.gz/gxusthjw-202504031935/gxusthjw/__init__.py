#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        __init__.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: gxusthjw包的__init__.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/30     revise
#       Jiwei Huang        0.0.1         2024/08/15     revise
#       Jiwei Huang        0.0.1         2024/08/31     revise
#       Jiwei Huang        0.0.1         2024/10/07     revise
#       Jiwei Huang        0.0.1         2024/10/15     revise
#       Jiwei Huang        0.0.1         2024/10/18     revise
#       Jiwei Huang        0.0.1         2024/10/21     revise
# ----------------------------------------------------------------
# 导包 ============================================================
from . import commons
from . import datalyzer
from . import datastruct
from . import filters
from . import fitters
from . import matplotlibs
from . import mechanalyzer
from . import smoothers
from . import statistics
from . import units
from . import xrd
# 声明 ============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
the python packages of gxusthjw.
"""

__all__ = [
    'run_tests',
    'commons',
    'datalyzer',
    'datastruct',
    'filters',
    'fitters',
    'matplotlibs',
    'mechanalyzer',
    'smoothers',
    'statistics',
    'units',
    'xrd',
]


# ==================================================================


def run_tests():
    """
    运行此包及其子包中的所有测试。

        运行方式：
            > import gxusthjw
            > gxusthjw.run_tests()
    """
    import unittest
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.')
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
# ==================================================================
