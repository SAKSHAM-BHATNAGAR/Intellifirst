import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 2), 5)
        self.assertEqual(calc.add(-1, 1), 0)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(3, 2), 1)
        self.assertEqual(calc.subtract(2, 5), -3)

if __name__ == '__main__':
    unittest.main()

# Write This In Terminal To Test The 
#pip install coverage
#coverage run -m unittest test_calculator.py
#coverage report
#coverage html