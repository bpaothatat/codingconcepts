#importing items in sibling path
from cmath import exp
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from linkedlist.doubly_linked_list import DoublyLinkedList
from exception.exceptions import EmptyError

class ArrayQueue:
    def __init__(self, limit=10):
        self._queue = []
        self._limit = limit
        self._front = None
        self._rear = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, element):
        if self._size == self._limit:
            self.resize()
        self._queue.append(element)
        if self._front is None:
            self._front = self._rear = 0
        else: 
            self._rear = self._size
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise EmptyError('Queue is empty')
        else:
            result = self._queue.pop(0)
            self._size -= 1
            if self._size == 0:
                self._front = self._rear = None
            else: 
                self._rear = self._size -1 
        return result

    def resize(self):
        expanded_queue = list(self._queue)
        self._limit = 2 * self._limit
        self._queue = expanded_queue
            
class LinkedListQueue:
    def __init__(self):
        self._queue = DoublyLinkedList()

    def __len__(self):
        return len(self._queue)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, element):
        self._queue.insertTail(element)

    def dequeue(self):
        if self.isEmpty():
            raise EmptyError('Queue empty')
        else:
            return self._queue.removeHead()