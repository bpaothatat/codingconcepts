from towers_of_hanoi import TowerOfHanoi
import unittest

class FactorialTest(unittest.TestCase):

    def test_non_integer(self):
        with self.assertRaises(TypeError) as context:
            TowerOfHanoi('test')
        self.assertTrue(context.exception, 'Expected integer greater than -1')

    def test_negative(self):
        with self.assertRaises(TypeError) as context:
            TowerOfHanoi(-1)
        self.assertTrue(context.exception, 'Expected integer greater than -1')

    def test_zero(self):
        self.assertEqual(TowerOfHanoi(0), [])

    def test_one(self):
         self.assertEqual(TowerOfHanoi(1), [(1, 1, 3)])

    def test_two(self):
       self.assertEqual(TowerOfHanoi(2), [(1, 1, 2), (2, 1, 3), (1, 2, 3)])

    def test_four(self):
      self.assertEqual(TowerOfHanoi(3), [(1, 1, 3), (2, 1, 2), (1, 3, 2), (3, 1, 3), (1, 2, 1), (2, 2, 3), (1, 1, 3)])

if __name__ == '__main__':
    unittest.main()