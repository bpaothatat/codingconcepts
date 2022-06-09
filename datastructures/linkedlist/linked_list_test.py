#importing items in sibling path
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from exception.exceptions import EmptyError
from linked_list import LinkedList
import unittest

class LinkedListTest(unittest.TestCase):

    def test_empty_list(self):
        list = LinkedList()
        with self.assertRaises(EmptyError) as context:
            list.removeHead()
        self.assertTrue(context.exception, 'Empty linked list')
        with self.assertRaises(EmptyError) as context:
            list.removeTail()
        self.assertTrue(context.exception, 'Empty linked list')
        self.assertEqual(len(list), 0)
        self.assertEqual(str(list), '')


    def test_add(self):
        list = LinkedList()
        list.insertAtHead(1)
        list.insertAtTail(2)
        list.insertAtHead(0)
        self.assertEqual(len(list), 3)
        self.assertEqual(str(list), '0,1,2')

    def test_remove(self):
        list = LinkedList()
        list.insertAtHead(1)
        list.insertAtTail(2)
        list.insertAtHead(0)
        self.assertEqual(list.removeHead(), 0)
        self.assertEqual(len(list), 2)
        self.assertEqual(str(list), '1,2')
        self.assertEqual(list.removeTail(), 2)
        self.assertEqual(len(list), 1)
        self.assertEqual(str(list), '1')
        self.assertEqual(list.removeHead(), 1)
        self.assertEqual(len(list), 0)
        self.assertEqual(str(list), '')
        list.insertAtHead(10)
        self.assertEqual(list.removeTail(), 10)
        self.assertEqual(len(list), 0)
        self.assertEqual(str(list), '')

if __name__ == '__main__':
    unittest.main()