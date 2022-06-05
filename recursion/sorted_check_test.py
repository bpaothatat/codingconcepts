from sorted_check import isArraySorted
import unittest

class FactorialTest(unittest.TestCase):

    def test_non_list(self):
        with self.assertRaises(TypeError) as context:
            isArraySorted('test')
        self.assertTrue(context.exception, 'Expected a list')

    def test_len_less_than_2(self):
        self.assertTrue(isArraySorted([]))
        self.assertTrue(isArraySorted([1]))

    def test_unsorted(self):
        self.assertFalse(isArraySorted([1,4,2]))
        self.assertFalse(isArraySorted([2,1]))

    def test_sorted(self):
        self.assertTrue(isArraySorted([1,2]))
        self.assertTrue(isArraySorted([1000,5000, 100000]))

if __name__ == '__main__':
    unittest.main()