import unittest

from tests.constants import (
    clean_up,
    set_up_utils, DEFAULT_METHOD_242, DEFAULT_METHOD_254,
)


class TestSequence(unittest.TestCase):
    """
    These tests should always work with an online controller.
    """

    def setUp(self):
        num = 254
        self.hplc_controller = set_up_utils(num, offline=False, runs=True)
        self.other_default = DEFAULT_METHOD_242 if num == 242 else DEFAULT_METHOD_254

    def tearDown(self):
        clean_up(self.hplc_controller)


if __name__ == "__main__":
    unittest.main()
