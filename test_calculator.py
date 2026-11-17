# https://github.com/Dddd559/lab11-RCK-ZD
# Partner 1: Zixian Dong
# Partner 2: Rishil Kodela

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(7, 3), 4)
        self.assertEqual(subtract(3, 7), -4)
        self.assertEqual(subtract(-2, -3), 1)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-3, 4), -12)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(2, 8), 4.0)
        self.assertAlmostEqual(div(-2, 8), -4.0)
        self.assertAlmostEqual(div(2, 0), 0.0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 1), 0)
        self.assertAlmostEqual(logarithm(0.5, 2), -1)

        for argument in (0, -1):
            with self.subTest(argument=argument):
                with self.assertRaises(ValueError):
                    logarithm(2, argument)

    def test_log_invalid_base(self):
        for base in (0, 1, -2):
            with self.subTest(base=base):
                with self.assertRaises(ValueError):
                    logarithm(base, 8)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
