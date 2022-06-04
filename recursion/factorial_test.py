from factorial import factorial
import unittest

class FactorialTest(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_two(self):
        self.assertEqual(factorial(2), 2)

    def test_ten(self):
        self.assertEqual(factorial(10), 3628800)

    def test_thirteen(self):
        self.assertEqual(factorial(13), 6227020800)

    def test_non_integer(self):
        with self.assertRaises(TypeError) as context:
            factorial('test')
        self.assertTrue(context.exception, 'Expected an integer')

if __name__ == '__main__':
    unittest.main()