import unittest

def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Ошибка: Деление на ноль!"
        return a / b
    else:
        return "Ошибка: Неверная операция!"

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(5, 3, '+'), 8)
        self.assertEqual(calculate(-1, 1, '+'), 0)

    def test_subtraction(self):
        self.assertEqual(calculate(5, 3, '-'), 2)
        self.assertEqual(calculate(5, 5, '-'), 0)

    def test_multiplication(self):
        self.assertEqual(calculate(5, 3, '*'), 15)
        self.assertEqual(calculate(-1, 5, '*'), -5)

    def test_division(self):
        self.assertEqual(calculate(6, 3, '/'), 2)
        self.assertEqual(calculate(5, 0, '/'), "Ошибка: Деление на ноль!")

    def test_invalid_operation(self):
        self.assertEqual(calculate(5, 3, '%'), "Ошибка: Неверная операция!")

if __name__ == "__main__":
    unittest.main()