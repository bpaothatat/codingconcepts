#importing items in sibling path
import sys
import os.path
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from exception.exceptions import EmptyError
from queue import ArrayQueue

class ArrayTest(unittest.TestCase):

    def test_empty_queue(self):
        queue = ArrayQueue()
        with self.assertRaises(EmptyError) as context:
            queue.dequeue()
        self.assertTrue(context.exception, 'Queue is empty')
        self.assertEqual(len(queue), 0)

if __name__ == '__main__':
    unittest.main()
