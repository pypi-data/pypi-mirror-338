#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        __init__.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: gxusthjw.units.textile包的__init__.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/02     revise
#       Jiwei Huang        0.0.1         2024/09/12     revise
# ------------------------------------------------------------------
# 导包 =============================================================
from .linear_density_unit import (LinearDensityUnit,
                                  LengthBasedLinearDensityUnit,
                                  WeightBasedLinearDensityUnit,
                                  DTex,
                                  Tex,
                                  Denier,
                                  MetricCount,
                                  den,
                                  dtex,
                                  tex,
                                  Nm)

# 声明 ============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
Assembling the classes and functions associated with `textile unit`.
"""

__all__ = ["LinearDensityUnit",
           "LengthBasedLinearDensityUnit",
           "WeightBasedLinearDensityUnit",
           "DTex",
           "Tex",
           "Denier",
           "MetricCount",
           "den",
           "dtex",
           "tex",
           "Nm"]
# ==================================================================
