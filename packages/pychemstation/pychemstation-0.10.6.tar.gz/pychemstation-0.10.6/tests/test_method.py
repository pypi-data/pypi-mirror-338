import random
import time
import unittest

from pychemstation.utils.macro import Command
from pychemstation.utils.method_types import (
    TimeTableEntry,
    MethodDetails,
    HPLCMethodParams,
)
from pychemstation.utils.tray_types import FiftyFourVialPlate
from tests.constants import (
    clean_up,
    set_up_utils,
    DEFAULT_METHOD,
    DEFAULT_METHOD_242,
    DEFAULT_METHOD_254,
    gen_rand_method,
)


class TestMethod(unittest.TestCase):
    """
    These tests should always work with an online controller.
    """

    def setUp(self):
        num = 242
        self.hplc_controller = set_up_utils(num, offline=False, runs=False)
        self.hplc_controller.send(
            Command.SAVE_METHOD_CMD.value.format(
                commit_msg="method saved by pychemstation"
            )
        )
        self.hplc_controller.switch_method(DEFAULT_METHOD)
        self.old_stop_time = self.hplc_controller.method_controller.get_stop_time()
        self.old_post_time = self.hplc_controller.method_controller.get_post_time()
        self.hplc_controller.method_controller.edit_stop_time(1)
        self.hplc_controller.method_controller.edit_post_time(0.5)
        self.other_default = DEFAULT_METHOD_242 if num == 242 else DEFAULT_METHOD_254

    def tearDown(self):
        self.hplc_controller.method_controller.edit_stop_time(self.old_stop_time)
        self.hplc_controller.method_controller.edit_post_time(self.old_post_time)
        clean_up(self.hplc_controller)

    def test_method_switch_load(self):
        self.hplc_controller.switch_method(DEFAULT_METHOD)
        self.assertEqual(
            DEFAULT_METHOD, self.hplc_controller.check_loaded_method()[:-2]
        )
        try:
            self.hplc_controller.switch_method("GENERAL-POROSHELL-JD")
            self.assertEqual(
                "GENERAL-POROSHELL-JD", self.hplc_controller.check_loaded_method()[:-2]
            )
        except Exception:
            self.hplc_controller.switch_method("WM_GENERAL_POROSHELL")
            self.assertEqual(
                "WM_GENERAL_POROSHELL", self.hplc_controller.check_loaded_method()[:-2]
            )

    def test_edit_method(self):
        self.hplc_controller.method_controller.switch(DEFAULT_METHOD)
        new_method = MethodDetails(
            name=DEFAULT_METHOD + ".M",
            timetable=[
                TimeTableEntry(start_time=1.0, organic_modifer=20.0, flow=0.65),
                TimeTableEntry(start_time=2.0, organic_modifer=30.0, flow=0.65),
                TimeTableEntry(start_time=2.5, organic_modifer=60.0, flow=0.65),
                TimeTableEntry(start_time=3.0, organic_modifer=80.0, flow=0.65),
                TimeTableEntry(start_time=3.5, organic_modifer=100.0, flow=0.65),
            ],
            stop_time=4.0,
            post_time=1.0,
            params=HPLCMethodParams(organic_modifier=5.0, flow=0.65),
        )
        try:
            self.hplc_controller.edit_method(new_method)
            self.assertEqual(new_method, self.hplc_controller.load_method())
        except Exception as e:
            self.fail(f"Should have not failed: {e}")

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
        for i, a_b in enumerate(zip(timetable, method_details.timetable)):
            method_a = a_b[0]
            method_b = a_b[1]
            self.assertAlmostEqual(method_a.start_time, method_b.start_time)
            self.assertAlmostEqual(method_a.organic_modifer, method_b.organic_modifer)
            self.assertAlmostEqual(method_a.flow, method_b.flow)

    def test_method_stall(self):
        for _ in range(5):
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
        for _ in range(5):
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

    def test_load_method(self):
        self.hplc_controller.method_controller.switch(DEFAULT_METHOD)
        new_method = gen_rand_method()
        try:
            self.hplc_controller.edit_method(new_method)
            loaded_method = self.hplc_controller.load_method()
            self.assertEqual(
                new_method.params.organic_modifier,
                loaded_method.params.organic_modifier,
            )
            self.assertEqual(
                new_method.timetable[0].organic_modifer,
                loaded_method.timetable[0].organic_modifer,
            )
            self.assertEqual(
                round(new_method.params.flow, 2), round(loaded_method.params.flow, 2)
            )
        except Exception as e:
            self.fail(f"Should have not failed: {e}")


if __name__ == "__main__":
    unittest.main()
