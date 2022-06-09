#importing items in sibling path
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from exception.exceptions import EmptyError

class Node:
    def __init__(self, data, next=None, previous=None):
        self._data = data
        self._next = next
        self._previous = previous

    def __str__(self):
        return str(self._data)


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def __len__(self):
        return self._count

    def __str__(self):
        result = ''
        current = self._head
        while current:
            if current._next:
                result += str(current) + ','
            else:
                result += str(current)
            current = current._next
        return result

    def insertHead(self, data):
        newNode = Node(data)
        if not self._head:
            self._head = self._tail = newNode
        else:
            newNode._next = self._head
            self._head._previous = newNode
            self._head = newNode
        self._count += 1
    
    def insertTail(self, data):
        if not self._head:
            self._head = self._tail = Node(data)
        else:
            current = self._head
            while current._next:
                current = current._next
            current._next = Node(data, previous=current)
            self._tail = current._next
        self._count += 1

    def removeHead(self):
        if not len(self) > 0:
            raise EmptyError('Empty doubly linked list')
        else:
            temp = self._head
            self._head = self._head._next
            if self._head:
                self._head._previous = None
            self._count -= 1
        return temp._data

    def removeTail(self):
        if not len(self) > 0:
            raise EmptyError('Empty doubly linked list')
        else:
            temp = self._tail
            self._tail = self._tail._previous
            if self._tail:
                self._tail._next = None
            else:
                self._head = None
            self._count -= 1
        return temp._data