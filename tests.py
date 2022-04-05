import unittest
from jpt import get_commission


class TestGetCommission(unittest.TestCase):
    def test_wrong_date_format(self):
        wrong_date = "2001-88-77"
        self.assertEqual(get_commission(wrong_date), "Please enter a valid date")

    def test_high_commission(self):
        high_commission_date = "2001-07-11"
        self.assertEqual(get_commission(high_commission_date), 15.0)

    def test_low_commission(self):
        low_commission_date = "2001-03-11"
        self.assertEqual(get_commission(low_commission_date), 10.0)
