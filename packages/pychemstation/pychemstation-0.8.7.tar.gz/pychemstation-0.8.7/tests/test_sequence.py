import time
import unittest
from typing import List

from pychemstation.analysis.chromatogram import AgilentChannelChromatogramData
from pychemstation.utils.tray_types import FiftyFourVialPlate
from tests.constants import (
    clean_up,
    set_up_utils,
    DEFAULT_METHOD_242,
    DEFAULT_METHOD_254,
    DEFAULT_SEQUENCE,
)


class TestSequence(unittest.TestCase):
    """
    These tests should always work with an online controller.
    """

    def setUp(self):
        num = 254
        self.hplc_controller = set_up_utils(num, offline=False, runs=True)
        self.other_default = DEFAULT_METHOD_242 if num == 242 else DEFAULT_METHOD_254
        self.loc1 = FiftyFourVialPlate.from_str("P1-A2")
        self.loc2 = FiftyFourVialPlate.from_str("P1-F2")
        self.hplc_controller.switch_sequence(DEFAULT_SEQUENCE)
        curr_seq = self.hplc_controller.load_sequence()
        self.assertEqual(self.loc1, curr_seq.rows[0].vial_location)
        self.assertEqual(self.loc2, curr_seq.rows[1].vial_location)

    def tearDown(self):
        clean_up(self.hplc_controller)

    def test_run_sequence_no_stall(self):
        self.hplc_controller.preprun()
        self.hplc_controller.run_sequence(stall_while_running=False)
        time_left, done = self.hplc_controller.check_sequence_complete()
        while not done:
            time.sleep(time_left / 2)
            time_left, done = self.hplc_controller.check_sequence_complete()
        chrom = self.hplc_controller.get_last_run_sequence_data()
        uv = self.hplc_controller.get_last_run_sequence_data(read_uv=True)
        reports = self.hplc_controller.get_last_run_sequence_reports()
        report_vials = [reports[0].vial_location, reports[1].vial_location]
        self.assertTrue(self.loc1 in report_vials)
        self.assertTrue(self.loc2 in report_vials)
        self.assertEqual(len(chrom), 2)
        self.assertEqual(len(uv), 2)

    def test_run_sequence(self):
        self.hplc_controller.preprun()
        self.hplc_controller.run_sequence(stall_while_running=True)
        chrom: List[AgilentChannelChromatogramData] = (
            self.hplc_controller.get_last_run_sequence_data()
        )
        uv = self.hplc_controller.get_last_run_sequence_data(read_uv=True)
        self.assertTrue(210 in uv[0].keys())
        self.assertTrue(len(chrom[0].A.x) > 0)
        reports = self.hplc_controller.get_last_run_sequence_reports()
        self.assertEqual(reports[0].signals[0].wavelength, 210)
        report_vials = [reports[0].vial_location, reports[1].vial_location]
        self.assertTrue(self.loc1 in report_vials)
        self.assertTrue(self.loc2 in report_vials)
        self.assertEqual(len(chrom), 2)
        self.assertEqual(len(uv), 2)


if __name__ == "__main__":
    unittest.main()
