#importing items in sibling path
import sys
import os.path
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from exception.exceptions import EmptyError
from queue import ArrayQueue, LinkedListQueue

class ArrayTest(unittest.TestCase):

    def test_empty_array_queue(self):
        queue = ArrayQueue()
        with self.assertRaises(EmptyError) as context:
            queue.dequeue()
        self.assertTrue(context.exception, 'Queue is empty')
        self.assertEqual(len(queue), 0)

    def test_array_queue(self):
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(len(queue), 0)


    def test_empty__linked_list_queue(self):
        queue = LinkedListQueue()
        with self.assertRaises(EmptyError) as context:
            queue.dequeue()
        self.assertTrue(context.exception, 'Queue is empty')
        self.assertEqual(len(queue), 0)

    def test_linked_list_queue(self):
            queue = LinkedListQueue()
            queue.enqueue(1)
            queue.enqueue(2)
            self.assertEqual(len(queue), 2)
            self.assertEqual(queue.dequeue(), 1)
            self.assertEqual(len(queue), 1)
            self.assertEqual(queue.dequeue(), 2)
            self.assertEqual(len(queue), 0)


if __name__ == '__main__':
    unittest.main()
