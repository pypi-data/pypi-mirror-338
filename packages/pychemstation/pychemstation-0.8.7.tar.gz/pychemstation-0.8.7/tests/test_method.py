import random
import time
import unittest

from pychemstation.utils.macro import Command
from pychemstation.utils.method_types import (
    TimeTableEntry,
)
from pychemstation.utils.tray_types import FiftyFourVialPlate
from tests.constants import (
    clean_up,
    set_up_utils,
    DEFAULT_METHOD,
    DEFAULT_METHOD_242,
    DEFAULT_METHOD_254,
)


class TestMethod(unittest.TestCase):
    """
    These tests should always work with an online controller.
    """

    def setUp(self):
        num = 254
        self.hplc_controller = set_up_utils(num, offline=False, runs=False)
        self.hplc_controller.send(
            Command.SAVE_METHOD_CMD.value.format(
                commit_msg="method saved by pychemstation"
            )
        )
        self.hplc_controller.switch_method(DEFAULT_METHOD)
        self.hplc_controller.method_controller.edit_stop_time(1)
        self.hplc_controller.method_controller.edit_post_time(0.5)
        self.old_method = self.hplc_controller.load_method()
        self.other_default = DEFAULT_METHOD_242 if num == 242 else DEFAULT_METHOD_254

    def tearDown(self):
        self.hplc_controller.edit_method(self.old_method)
        clean_up(self.hplc_controller)

    def test_update_method_components(self):
        new_flow = random.randint(1, 10) / 10
        self.hplc_controller.method_controller.edit_flow(new_flow=new_flow)
        new_post_time = random.randint(1, 6)
        self.hplc_controller.method_controller.edit_post_time(
            new_post_time=new_post_time
        )
        new_stop_time = random.randint(1, 20)
        self.hplc_controller.method_controller.edit_stop_time(
            new_stop_time=new_stop_time
        )
        new_om = random.randint(1, 50)
        self.hplc_controller.method_controller.edit_initial_om(new_om=new_om)
        method_details = self.hplc_controller.load_method()
        self.assertEqual(method_details.params.flow, new_flow)
        self.assertEqual(method_details.post_time, new_post_time)
        self.assertEqual(method_details.stop_time, new_stop_time)
        self.assertEqual(method_details.params.organic_modifier, new_om)

    def test_update_only_timetable(self):
        start_time_1 = random.randint(1, 10)
        starting_og = random.randint(1, 50)
        timetable_flow = random.randint(1, 10) / 10
        timetable = [
            TimeTableEntry(
                start_time=start_time_1,
                organic_modifer=starting_og,
                flow=timetable_flow,
            ),
            TimeTableEntry(
                start_time=start_time_1 + 5, organic_modifer=78, flow=1 - timetable_flow
            ),
        ]
        self.hplc_controller.method_controller.edit_method_timetable(timetable)
        method_details = self.hplc_controller.load_method()
        self.assertEqual(method_details.timetable, timetable)

    def test_method_stall(self):
        for _ in range(2):
            self.hplc_controller.run_method(
                experiment_name="test_experiment", stall_while_running=False
            )
            time_left, done = self.hplc_controller.check_method_complete()
            while not done:
                time.sleep(time_left / 2)
                time_left, done = self.hplc_controller.check_method_complete()
            chrom = self.hplc_controller.get_last_run_method_data()
            uv = self.hplc_controller.get_last_run_method_data(read_uv=True)
            repos = self.hplc_controller.get_last_run_method_report()
            self.assertEqual(repos.vial_location, FiftyFourVialPlate.from_str("P1-F2"))
            self.assertEqual(repos.signals[0].wavelength, 210)
            self.assertIsNotNone(
                repos.signals[0].data,
            )
            self.assertTrue(210 in uv.keys())
            self.assertTrue(len(chrom.A.x) > 0)

    def test_method_no_stall(self):
        for _ in range(2):
            self.hplc_controller.run_method(experiment_name="test_experiment")
            chrom = self.hplc_controller.get_last_run_method_data()
            uv = self.hplc_controller.get_last_run_method_data(read_uv=True)
            repos = self.hplc_controller.get_last_run_method_report()
            self.assertEqual(repos.vial_location, FiftyFourVialPlate.from_str("P1-F2"))
            self.assertEqual(repos.signals[0].wavelength, 210)
            self.assertIsNotNone(
                repos.signals[0].data,
            )
            self.assertTrue(210 in uv.keys())
            self.assertTrue(len(chrom.A.x) > 0)


if __name__ == "__main__":
    unittest.main()
