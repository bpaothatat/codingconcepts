from exceptions import EmptyError
from doubly_linked_list import DoublyLinkedList
import unittest

class LinkedListTest(unittest.TestCase):

    def test_empty_list(self):
        list = DoublyLinkedList()
        with self.assertRaises(EmptyError) as context:
            list.removeHead()
        self.assertTrue(context.exception, 'Empty doubly linked list')
        with self.assertRaises(EmptyError) as context:
            list.removeTail()
        self.assertTrue(context.exception, 'Empty doubly linked list')
        self.assertEqual(len(list), 0)
        self.assertEqual(str(list), '')


    def test_add(self):
        list = DoublyLinkedList()
        list.insertHead(1)
        list.insertTail(2)
        list.insertHead(0)
        self.assertEqual(len(list), 3)
        self.assertEqual(str(list), '0,1,2')

    def test_remove(self):
        list = DoublyLinkedList()
        list.insertHead(1)
        list.insertTail(2)
        list.insertHead(0)
        self.assertEqual(list.removeHead(), 0)
        self.assertEqual(len(list), 2)
        self.assertEqual(str(list), '1,2')
        self.assertEqual(list.removeTail(), 2)
        self.assertEqual(len(list), 1)
        self.assertEqual(str(list), '1')
        self.assertEqual(list.removeHead(), 1)
        self.assertEqual(len(list), 0)
        self.assertEqual(str(list), '')
        list.insertHead(10)
        self.assertEqual(list.removeTail(), 10)
        print(list)
        self.assertEqual(len(list), 0)
        self.assertEqual(str(list), '')

if __name__ == '__main__':
    unittest.main()