#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        test_cre_datalyzer.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试cre_datalyzer.py。
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
#       Jiwei Huang        0.0.1         2024/09/12     revise
#       Jiwei Huang        0.0.1         2024/09/16     revise
#       Jiwei Huang        0.0.1         2024/10/12     revise
#       Jiwei Huang        0.0.1         2024/10/13     revise
#       Jiwei Huang        0.0.1         2024/10/17     finish
# ------------------------------------------------------------------
# 导包 =============================================================
import math
import os
import re
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from .cre_datalyzer import CreMechDataAnalyzer


# ==================================================================
class TestCreDatalyzer(unittest.TestCase):
    """
    测试cre_datalyzer.py。
    """

    # --------------------------------------------------------------------
    def setUp(self):
        """
        Hook method for setting up the test fixture before exercising it.
        """
        # --------------------------------------------------------
        this_file = __file__
        print("this file: %s" % this_file)
        this_file_path, this_file_name = os.path.split(this_file)
        print("this file name: %s" % this_file_name)
        print("this_file_path: %s" % this_file_path)
        # --------------------------------------------------------
        test_data_path = "test_data"
        test_file_name = "2-3 dry 9.8 15.xlsx"
        test_file = os.path.join(this_file_path, test_data_path, test_file_name)
        print(f"test_file:{test_file}")
        # --------------------------------------------------------
        data = pd.read_excel(test_file, header=0, engine="openpyxl")
        height = float(re.sub(r"[^\d.]", "", data.iat[0, 2]))
        diameter = float(re.sub(r"\D", "", data.iat[0, 3]))
        new_data = data.iloc[1:]

        nos = np.asarray(new_data.iloc[:, 0], dtype=np.int64)
        times = np.asarray(new_data.iloc[:, 1], dtype=np.float64)
        displacements = np.asarray(new_data.iloc[:, 2], dtype=np.float64)
        force = np.asarray(new_data.iloc[:, 3], dtype=np.float64)

        print(f"height:{height},diameter={diameter}")
        print(f"nos:{nos}")
        print(f"times:{times}")
        print(f"displacements:{displacements}")
        print(f"force:{force}")

        # 将字符串转换为Path对象
        path = Path(test_file)
        # 获取文件名
        file_name = path.name
        # 获取文件所在文件夹名
        folder_name = path.parent.name
        # 获取文件所在文件夹的上层文件夹名
        parent_folder_name = (
            path.parent.parent.name if path.parent.parent != Path(".") else "根目录"
        )
        self.analyzer = CreMechDataAnalyzer(
            displacements,
            force,
            times,
            displacement_unit="mm",
            force_unit="N",
            time_unit="min",
            clamp_distance=height,
            clamp_distance_unit="mm",
            cross_area=(math.pi * diameter**2) / 4,
            cross_area_unit="mm^2",
            specimen_name=f"{parent_folder_name}_{folder_name}",
            specimen_no=0,
            raw_file_name=file_name,
        )

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

    def test_init0(self):
        displacements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        forces = [0.1, 0.2, 0.3, 0.4, 0.42, 0.43, 0.45, 0.46, 0.47, 0.5]
        assert len(displacements) == len(forces)
        times = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.10]
        assert len(times) == len(displacements)
        print("\n\n-----------------------------------------------------")
        cre_datalyzer = CreMechDataAnalyzer(displacements, forces)
        cre_datalyzer.data_logger.print(
            {
                "display.max_columns": None,
                "display.max_rows": None,
                "display.max_colwidth": None,
            }
        )

        this_path = os.path.abspath(os.path.dirname(__file__))
        out_path = os.path.join(this_path, "test_out")
        if not os.path.exists(out_path):
            os.makedirs(out_path)

        csv_file = os.path.join(out_path, "cre_datalyzer.csv")
        print(csv_file)

        cre_datalyzer.data_logger.to_csv(csv_file)
        html_file = os.path.join(out_path, "cre_datalyzer.html")
        cre_datalyzer.data_logger.to_html(html_file)

    def test_init1(self):
        pass

    # noinspection PyUnresolvedReferences
    def test_calibrate_times(self):
        self.analyzer.calibrate_times()
        # noinspection PyUnresolvedReferences
        plt.plot(self.analyzer.data_nos, self.analyzer.times_calibrated)
        plt.show()
        # noinspection PyUnresolvedReferences
        print(self.analyzer.real_signal_interval)
        # noinspection PyUnresolvedReferences
        print(self.analyzer.real_signal_frequency)
        # noinspection PyUnresolvedReferences
        self.assertEqual(
            self.analyzer.real_signal_interval,
            self.analyzer.data_logger.get("real_signal_interval").item(),
        )
        self.assertEqual(
            self.analyzer.real_signal_frequency,
            self.analyzer.data_logger.get("real_signal_frequency").item(),
        )
        self.assertTrue(
            np.array_equal(
                self.analyzer.times_calibrated,
                self.analyzer.data_logger.get("times_calibrated"),
            )
        )

    # noinspection PyUnresolvedReferences
    def test_calibrate_displacements(self):
        self.analyzer.calibrate_displacements()
        # noinspection PyUnresolvedReferences
        plt.plot(
            self.analyzer.displacements_calibrated,
            self.analyzer.displacements_calibrated,
        )
        plt.show()
        # noinspection PyUnresolvedReferences
        print(self.analyzer.real_displacement_rate)
        # noinspection PyUnresolvedReferences
        print(self.analyzer.real_strain_rate)
        # noinspection PyUnresolvedReferences
        print(self.analyzer.real_strain_percentage)
        print(self.analyzer.real_speed)
        self.assertEqual(
            self.analyzer.real_displacement_rate,
            self.analyzer.data_logger.get("real_displacement_rate").item(),
        )
        self.assertEqual(
            self.analyzer.real_strain_rate,
            self.analyzer.data_logger.get("real_strain_rate").item(),
        )
        self.assertEqual(
            self.analyzer.real_strain_percentage,
            self.analyzer.data_logger.get("real_strain_percentage").item(),
        )
        self.assertEqual(
            self.analyzer.real_speed,
            self.analyzer.data_logger.get("real_speed").item(),
        )
        self.assertTrue(
            np.array_equal(
                self.analyzer.displacements_calibrated,
                self.analyzer.data_logger.get("displacements_calibrated"),
            )
        )

    # noinspection PyUnresolvedReferences
    def test_calibrate_forces(self):
        self.analyzer.calibrate_forces()
        plt.plot(
            self.analyzer.displacements_calibrated, self.analyzer.forces_calibrated
        )
        plt.show()
        self.assertTrue(
            np.array_equal(
                self.analyzer.displacements_calibrated,
                self.analyzer.data_logger.get("displacements_calibrated"),
            )
        )
        self.assertTrue(
            np.array_equal(
                self.analyzer.times_calibrated,
                self.analyzer.data_logger.get("times_calibrated"),
            )
        )
        self.assertTrue(
            np.array_equal(
                self.analyzer.forces_calibrated,
                self.analyzer.data_logger.get("forces_calibrated"),
            )
        )

    def test_strains_stress(self):
        self.analyzer.calibrate_forces()
        plt.plot(self.analyzer.strains, self.analyzer.stress)
        plt.show()

    # noinspection PyUnresolvedReferences
    def test_data_trimmed(self):
        self.analyzer.calibrate_forces()
        print(self.analyzer.data_trimmed())
        self.assertTrue(
            np.array_equal(
                self.analyzer.strains_trimmed,
                self.analyzer.data_logger.get("strains_trimmed"),
            )
        )
        self.assertTrue(
            np.array_equal(
                self.analyzer.strain_percentages_trimmed,
                self.analyzer.data_logger.get("strain_percentages_trimmed"),
            )
        )
        self.assertTrue(
            np.array_equal(
                self.analyzer.stress_trimmed,
                self.analyzer.data_logger.get("stress_trimmed"),
            )
        )
        self.assertTrue(
            np.array_equal(
                self.analyzer.times_trimmed,
                self.analyzer.data_logger.get("times_trimmed"),
            )
        )

        plt.plot(self.analyzer.strains_trimmed, self.analyzer.stress_trimmed)
        plt.show()
        plt.plot(self.analyzer.strain_percentages_trimmed, self.analyzer.stress_trimmed)
        plt.show()

    # noinspection PyUnresolvedReferences
    def test_initial_modulus(self):
        self.analyzer.calibrate_forces()
        self.analyzer.data_trimmed()
        print(f"self.strains_trimmed:{self.analyzer.strains_trimmed}")
        print(f"self.stress_trimmed:{self.analyzer.stress_trimmed}")
        print(f"self.times_trimmed:{self.analyzer.times_trimmed}")
        plt.plot(self.analyzer.strains_trimmed, self.analyzer.stress_trimmed)
        plt.show()
        print(self.analyzer.initial_modulus)

    # noinspection PyStatementEffect
    def test_yield_region(self):
        self.analyzer.calibrate_forces()
        self.analyzer.data_trimmed()
        self.analyzer.calibrate_yield_region
        print(f"self.analyzer.breaking_strength:{self.analyzer.breaking_strength}")
        print(f"self.analyzer.breaking_elongation:{self.analyzer.breaking_elongation}")
        print(f"self.analyzer.toughness:{self.analyzer.toughness}")
        print(f"self.analyzer.breaking_work:{self.analyzer.breaking_work}")

    def test_calibrate_yield_point(self):
        self.analyzer.calibrate_forces()
        self.analyzer.data_trimmed()
        print(self.analyzer.calibrate_yield_point(is_plot=True))

    def test_calibrate_hardening_point(self):
        self.analyzer.calibrate_forces()
        self.analyzer.data_trimmed()
        print(self.analyzer.calibrate_hardening_point(is_plot=True))


if __name__ == "__main__":
    unittest.main()
