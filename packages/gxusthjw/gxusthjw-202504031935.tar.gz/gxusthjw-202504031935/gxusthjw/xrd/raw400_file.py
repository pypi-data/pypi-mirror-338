#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        raw400_file.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 解析并读取RAW4.00文件。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2024/09/25     revise
# ------------------------------------------------------------------
# 导包 ==============================================================
import os
from typing import Union, Optional

import pandas as pd

from ..commons import (FileObject,
                       FileInfo,
                       list_files_with_suffix)

# 定义 ============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
Processing xrd data file with RAW4.00 format.
"""

__all__ = [
    'XrdRaw400File',
    'XrdRaw400Folder'
]


# ==================================================================
class XrdRaw400File(FileObject):
    """
    类`XrdRaw400File`表征“RAW4.00格式的XRD数据文件”。

    """

    def __init__(self, file: Union[str, FileInfo],
                 encoding: Optional[str] = None,
                 **kwargs):
        """
        类`XrdRaw400File`的初始化方法。

        :param file_path: 数据文件的完整路径。
        :param encoding: RAW4.00格式的XRD数据文件的编码。
        :param kwargs: 其他关键字参数。
        """
        super(XrdRaw400File, self).__init__(file, encoding, **kwargs)
        self.__name = self.file_base_name
        self.read_parse()

    @property
    def name(self) -> str:
        """
        返回数据文件的名称。

        :return: 数据文件的名称。
        """
        return self.__name

    def read_parse(self) -> None:
        """
        读取并解析RAW4.00格式的数据文件的内容。
        """
        # 打开文件
        with open(self.file_full_path, 'r', encoding=self.encoding) as file:
            # 读取所有行。
            lines = file.readlines()

        # 查找[data]的位置
        start_index = -1
        for i, line in enumerate(lines):
            if line.strip().lower() == '[data]':
                start_index = i + 1  # 跳过[data]这一行
                break

        if start_index < 0:
            raise ValueError("The [data] tag was not found")

        column_names = [f"{self.name}_{col.strip()}" for col in lines[start_index].split(',') if col.strip()]

        # 去除空行或只包含空格的行，并且去除每行末尾的空字符串
        data_lines = [
            [item for item in line.strip().split(',') if item]  # 过滤掉空字符串
            for line in lines[start_index + 1:]
            if line.strip()  # 只处理非空行
        ]

        # 创建DataFrame
        df = pd.DataFrame(data=data_lines, columns=column_names)
        setattr(self, 'data', df)


class XrdRaw400Folder(object):
    """
    类`XrdRaw400Folder`表征“RAW4.00格式的XRD数据文件的文件夹”
    """

    def __init__(self, folder: str,
                 encoding: Optional[str] = None,
                 **kwargs):
        """
        类`XrdRaw400Folder`的初始化方法。

        :param folder: RAW4.00格式的XRD数据文件所在文件夹的路径。
        :param encoding: RAW4.00格式的XRD数据文件的编码。
        :param kwargs: 其他关键字参数。
        """
        self.__folder = folder
        self.__encoding = encoding
        self.__kwargs = kwargs

    @property
    def list_txt_files(self):
        """
        返回此文件夹下所有的txt文件。

        :return: 此文件夹下所有的txt文件。
        """
        return list_files_with_suffix('.txt', self.__folder)

    def read_txt(self, files=None):
        """
        读取txt文件，并返回一个列表，列表中的元素为XrdRaw400File对象。

        :param files: 要读取文件的列表。
        """
        if files is None:
            files = self.list_txt_files
        res = []
        for file in files:
            res.append(XrdRaw400File(file, self.__encoding, **self.__kwargs))

        setattr(self, 'file_objects', res)
        return res

    # noinspection PyUnresolvedReferences
    def to_csv(self, file: str):
        """
        将所述数据文件输出至指定的文件。

        :param file: 输出文件的完整路径。
        """
        if not hasattr(self, 'file_objects'):
            self.read_txt()

        datas = []

        for file_obj in self.file_objects:
            datas.append(file_obj.data)

        df = pd.concat(datas, axis=1)
        # 确保目录存在
        directory = os.path.dirname(file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        df.to_csv(file, index=False)
