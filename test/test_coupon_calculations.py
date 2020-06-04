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
    def test_price_under_ten(self):
        self.assertAlmostEqual(cc.calculate_price(7.99, 5, 10), 9.16, places=2)
        self.assertAlmostEqual(cc.calculate_price(7.99, 5, 15), 9.00, places=2)
        self.assertAlmostEqual(cc.calculate_price(7.99, 5, 20), 8.84, places=2)
        self.assertAlmostEqual(cc.calculate_price(7.99, 10, 10), 4.39, places=2)

    def test_price_between_ten_thirty(self):
        self.assertAlmostEqual(cc.calculate_price(17.99, 5, 10), 20.82, places=2)
        self.assertAlmostEqual(cc.calculate_price(17.99, 5, 15), 20.13, places=2)
        self.assertAlmostEqual(cc.calculate_price(17.99, 5, 20), 19.44, places=2)
        self.assertAlmostEqual(cc.calculate_price(17.99, 10, 10), 13.93, places=2)

    def test_price_between_thirty_fifty(self):
        self.assertAlmostEqual(cc.calculate_price(41.27, 5, 10), 47.27, places=2)
        self.assertAlmostEqual(cc.calculate_price(41.27, 5, 15), 45.35, places=2)
        self.assertAlmostEqual(cc.calculate_price(41.27, 5, 20), 39.18, places=2)
        self.assertAlmostEqual(cc.calculate_price(41.27, 10, 10), 38.26, places=2)

    def test_price_over_fifty(self):
        self.assertAlmostEqual(cc.calculate_price(52.99, 5, 10), 58.45, places=2)
        self.assertAlmostEqual(cc.calculate_price(59.99, 5, 15), 62.21, places=2)
        self.assertAlmostEqual(cc.calculate_price(62.99, 5, 20), 61.84, places=2)
        self.assertAlmostEqual(cc.calculate_price(78.26, 5, 20), 62.12, places=2)
        self.assertAlmostEqual(cc.calculate_price(84.99, 10, 15), 67.57, places=2)
        self.assertAlmostEqual(cc.calculate_price(100.38, 10, 10), 86.22, places=2)


if __name__ == '__main__':
    unittest.main()
