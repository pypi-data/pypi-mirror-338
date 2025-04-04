#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        __init__.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: gxusthjw.datastruct包的__init__.py。
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
# ----------------------------------------------------------------
# 导包 ============================================================
from .data_2d import Data2d
from .data_2d_region import Data2dRegion

# 声明 ============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
Assembling the classes and functions associated with `data structure`.
"""

__all__ = [
    'Data2d',
    'Data2dRegion',
]
# 定义 ============================================================
