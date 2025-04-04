#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        __init__.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: gxusthjw.commons包的__init__.py。
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
# ----------------------------------------------------------------
# 导包 ============================================================
from .array_utils import (
    is_sorted,
    is_sorted_ascending,
    is_sorted_descending,
    reverse,
    Ordering,
    is_equals_of,
    sort,
    find_closest_index,
    find_crossing_index,
    find_index_range,
)
from .dataframe_utils import (
    ItemDataType,
    create_df_from_dict,
    create_df_from_item,
    merge_dfs,
)
from .file_object import (
    get_file_encoding_chardet,
    get_file_info,
    get_file_info_of_module,
    FileInfo,
    FileObject,
)
from .file_path import (
    sep_file_path,
    join_file_path,
    list_files_with_suffix,
    print_files_and_folders,
    list_files_and_folders,
    get_this_path,
    get_project_path,
    get_root_path,
)
from .logger_object import LoggerObject, get_properties
from .typings import (
    Number,
    NumberArrayLike,
    NumberSequence,
    Numbers,
    Numeric,
    is_number,
    is_number_array_like,
    is_number_sequence,
    is_numbers,
    is_numeric,
)
from .unique_object import (
    UniqueIdentifierObject,
    unique_string,
    random_string,
    date_string,
)

# 声明 ============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
The common functions and classes of the `gxusthjw` python packages.
"""

__all__ = [
    "is_sorted",
    "is_sorted_ascending",
    "is_sorted_descending",
    "reverse",
    "is_equals_of",
    "Ordering",
    "sort",
    "find_closest_index",
    "find_crossing_index",
    "find_index_range",
    "ItemDataType",
    "create_df_from_item",
    "create_df_from_dict",
    "merge_dfs",
    "get_file_encoding_chardet",
    "get_file_info",
    "get_file_info_of_module",
    "FileInfo",
    "FileObject",
    "sep_file_path",
    "join_file_path",
    "list_files_and_folders",
    "print_files_and_folders",
    "list_files_with_suffix",
    "get_root_path",
    "get_project_path",
    "get_this_path",
    "get_properties",
    "LoggerObject",
    "Number",
    "is_number",
    "NumberArrayLike",
    "is_number_array_like",
    "NumberSequence",
    "is_number_sequence",
    "Numbers",
    "is_numbers",
    "Numeric",
    "is_numeric",
    "random_string",
    "unique_string",
    "date_string",
    "UniqueIdentifierObject",
]
# 定义 ============================================================
