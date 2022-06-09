#importing items in sibling path
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from exception.exceptions import EmptyError
from stack import ArrayStack, LinkedListStack
import unittest

class StackTest(unittest.TestCase):

    def test_empty_stack(self):
        stack = ArrayStack()
        with self.assertRaises(EmptyError) as context:
            stack.pop()
        self.assertTrue(context.exception, 'Stack is empty')
        self.assertEqual(stack.peek(), None)
        self.assertEqual(len(stack), 0)

class StackTest(unittest.TestCase):

    def test_empty_stack(self):
        stack = LinkedListStack()
        with self.assertRaises(EmptyError) as context:
            stack.pop()
        self.assertTrue(context.exception, 'Stack is empty')
        self.assertEqual(stack.peek(), None)
        self.assertEqual(len(stack), 0)


if __name__ == '__main__':
    unittest.main()