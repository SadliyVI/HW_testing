import unittest
from unittest import TestCase
from parameterized import parameterized

from task_1_1 import discriminant, solution

class TestQuadraticEquation(TestCase):
    # Тест функции discriminant()
    @parameterized.expand([
        # (a, b, c, expected_discriminant)
        (1, 8, 15, 4),      # D = 8² -4 * 1* 15 = 64 - 60 = 4
        (1, -13, 12, 121),  # D = (-13)² -4 * 1* 12 = 169 -48 = 121
        (-4, 28, -49, 0),   # D = 28² -4 * (-4) * (-49) = 784 -784 = 0
        (1, 0, -16, 64),    # D = 0² -4 * 1 * (-16) = 64
        (2, -5, 3, 1),      # D = (-5)² -4 * 2 * 3 =25 - 24 = 1
        (1, 1, 1, -3)       # D = 1² - 4 * 1 * 1 = 1 - 4 = -3
    ])
    def test_discriminant_calculation(self, a, b, c, expected_discriminant):
        self.assertEqual(
            discriminant(a, b, c),
            expected_discriminant
        )

    # Тест функции solution()
    ''' 1 проверка D > 0 -> def test_two_roots(): Два различных корня
        2 проверка D = 0 -> def test_one_root(): Один корень
        3 проверка D < 0 -> def test_no_roots(): Нет корней
        4 проверка  на a = 0 -> test_zero_divided(): (ожидается ошибка 
        -> ZeroDivisionError).        
    '''

    def test_two_roots(self):
        # Тест с двумя корнями
        self.assertEqual(solution(1, 8, 15), (-3, -5))
        self.assertEqual(solution(1, -13, 12), (12, 1))
        self.assertEqual(solution(1, 0, -16), (4, -4))
        self.assertEqual(solution(2, -5, 3), (1.5, 1.0))

    def test_one_root(self):
        self.assertEqual(solution(-4, 28, -49), 3.5)

    def test_no_roots(self):
        result = solution(1, 1, 1)
        self.assertIsNone(result, 'No roots')

    def test_zero_divided(self):
        with self.assertRaises(ZeroDivisionError):
            solution(0, 2, 3)


