"""
Program: test_coupon_calculations.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020
Purpose: test the nested if statement as well as assertAlmostEqual
"""

import unittest
import unittest.mock as mock
from store import coupon_calculations as cc


class MyTestCase(unittest.TestCase):
    def test_price_under_10(self):
        self.assertAlmostEqual(cc.calculate_price(7.99, 5, 10), 9.16, places=2)
        self.assertAlmostEqual(cc.calculate_price(7.99, 5, 15), 9.00, places=2)
        self.assertAlmostEqual(cc.calculate_price(7.99, 5, 20), 8.84, places=2)
        self.assertAlmostEqual(cc.calculate_price(7.99, 10, 10), 4.39, places=2)


if __name__ == '__main__':
    unittest.main()
