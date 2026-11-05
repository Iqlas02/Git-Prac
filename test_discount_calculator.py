import unittest
from discount_calculator import calculate_discount


class TestDiscountCalculator(unittest.TestCase):

    def test_ten_percent_discount(self):
        self.assertEqual(calculate_discount(100, 10), 90.00)

    def test_twenty_percent_discount(self):
        self.assertEqual(calculate_discount(250, 20), 200.00)

    def test_zero_percent_discount(self):
        self.assertEqual(calculate_discount(100, 0), 100.00)

    def test_hundred_percent_discount(self):
        self.assertEqual(calculate_discount(100, 100), 0.00)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_discount(-100, 10)

    def test_negative_discount(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, -10)

    def test_discount_above_100(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, 110)


if __name__ == "__main__":
    unittest.main()