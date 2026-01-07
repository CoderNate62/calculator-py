import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(4, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)

    def test_log(self):
        import math
        self.assertAlmostEqual(self.calc.log(math.e), 1)
        with self.assertRaises(ValueError):
            self.calc.log(0)

    def test_trig(self):
        import math
        self.assertAlmostEqual(self.calc.sin(0), 0)
        self.assertAlmostEqual(self.calc.cos(0), 1)
        self.assertAlmostEqual(self.calc.tan(0), 0)

if __name__ == '__main__':
    unittest.main()
