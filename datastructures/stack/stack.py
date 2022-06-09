#importing items in sibling path
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from linkedlist.linked_list import *
from exception.exceptions import EmptyError

class ArrayStack:
    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return str(self._stack)

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if len(self) == 0:
            raise EmptyError('Stack is empty')
        else:
            return self._stack.pop()

    def peek(self):
        result = None
        if len(self) > 0:
            result = self._stack[-1]
        return result

    def size(self):
        return len(self)

class LinkedListStack():
    def __init__(self):
        self._stack = LinkedList()

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return str(self._stack)

    def push(self, item):
        self._stack.insertAtHead(item)

    def pop(self):
        return self._stack.removeHead()

    def peek(self):
        return self._stack._head

    def size(self):
        return len(self)