import unittest
from Calculator import (
    add, subtract, multiply, divide, is_even,
    factorial, fibonacci, power, is_prime, gcd
)

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertIsInstance(add(1, 2), int)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 1), -1)
        self.assertIsInstance(subtract(10, 5), int)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertIsInstance(multiply(2.5, 4), float)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertIsInstance(is_even(4), bool)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(0), 0)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertIsInstance(power(2, 3), int)

    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        self.assertIsInstance(is_prime(7), bool)

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(20, 8), 4)
        self.assertIsInstance(gcd(10, 5), int)

if __name__ == '__main__':
    unittest.main()
