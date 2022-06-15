from hashing import contains_duplicate
import unittest

class HashingTest(unittest.TestCase):

    def test_contains_duplciated(self):
        self.assertFalse(contains_duplicate([]))
        self.assertFalse(contains_duplicate([1]))
        self.assertTrue(contains_duplicate([1, 1]))
        self.assertFalse(contains_duplicate([1, 2 ,3, 4]))
        self.assertTrue(contains_duplicate([1, 2, 3, 4, 1]))

if __name__ == '__main__':
    unittest.main()