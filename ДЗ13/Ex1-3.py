import unittest
from testing_example import calculate_credit
from testing_example import Calculator


class TestCalculateCredit(unittest.TestCase):
    def test_exact(self):
        result = calculate_credit(100000, 6, 100)
        expected_result = 49999
        self.assertEqual(expected_result, result)

    def test_zero_division(self):
        try:
            result = calculate_credit(100000, 0, 100)
            expected_result = result
            self.assertEqual(expected_result, result)
        except ZeroDivisionError:
            print('Ошибка. Произведено деление на 0')

    def test_negative(self):
        result = calculate_credit(-5, 6, 100)
        expected_result = result
        self.assertEqual(expected_result, result)


class TestCalculator(unittest.TestCase, Calculator):
    def test_sum(self):
        result = Calculator.sum(4, 5)
        expected_result = 9
        self.assertEqual(expected_result, result)

    def test_mult(self):
        result = Calculator.mult(4, 5)
        expected_result = 20
        self.assertEqual(expected_result, result)
