from bit_strings import bitStrings
import unittest

class BitStringsTest(unittest.TestCase):

    def test_non_integer(self):
        with self.assertRaises(TypeError) as context:
            bitStrings('test')
        self.assertTrue(context.exception, 'Expected an integer')
    
    def test_length_zero(self):
        self.assertEqual(bitStrings(0), [])

    def test_length_one(self):
        self.assertEqual(bitStrings(1), ["0", "1"])

    def test_length_two(self):
        self.assertEqual(bitStrings(2), ['00', '01', '10', '11'])

    def test_length_three(self):
        self.assertEqual(bitStrings(3), ['000', '001', '010', '011', '100', '101', '110', '111'])

if __name__ == '__main__':
    unittest.main()