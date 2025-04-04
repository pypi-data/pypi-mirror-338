#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        __init__.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: gxusthjw.xrd包的__init__.py。
#                                  承载“XRD”相关的类和函数。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/30     revise
#       Jiwei Huang        0.0.1         2024/08/20     revise
# ----------------------------------------------------------------
# 导包 ============================================================
from .parse_xrdml import parse_xrdml, xrdml_to_raw
from .raw400_file import XrdRaw400File, XrdRaw400Folder

# 声明 ============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
Assembling classes and functions associated with `XRD`.
"""

__all__ = [
    'parse_xrdml',
    'xrdml_to_raw',
    'XrdRaw400File',
    'XrdRaw400Folder'
]
# ==================================================================
