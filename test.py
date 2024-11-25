import unittest
from calculator import Calculator  
import tkinter as tk

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.calculator.result_var.set("")  # Сбросим результат перед каждым тестом

    def test_append_to_expression(self):
        self.calculator.append_to_expression('5')
        self.assertEqual(self.calculator.result_var.get(), '5')

        self.calculator.append_to_expression('+')
        self.assertEqual(self.calculator.result_var.get(), '5+')

        self.calculator.append_to_expression('3')
        self.assertEqual(self.calculator.result_var.get(), '5+3')

    def test_clear(self):
        self.calculator.result_var.set("1234")
        self.calculator.clear()
        self.assertEqual(self.calculator.result_var.get(), "")

    def test_calculate_valid_expression(self):
        self.calculator.result_var.set("5+3")
        self.calculator.calculate()
        self.assertEqual(self.calculator.result_var.get(), "8")

    def test_calculate_invalid_expression(self):
        self.calculator.result_var.set("5/0")
        self.calculator.calculate()
        self.assertEqual(self.calculator.result_var.get(), "Ошибка")

    def test_calculate_syntax_error(self):
        self.calculator.result_var.set("5+")
        self.calculator.calculate()
        self.assertEqual(self.calculator.result_var.get(), "Ошибка")

if __name__ == "__main__":
    unittest.main()