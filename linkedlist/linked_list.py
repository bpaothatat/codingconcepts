from exceptions import EmptyError
from node import Node

class LinkedList:
    def __init__(self):
        self._head = None
        self._count = 0

    def __len__(self):
        return self._count

    def __str__(self):
        current = self._head
        result = ''

        while current:
            if current._next:
                result += str(current) + ','
            else:
                result += str(current)
            current = current._next
        return result

    def insertAtHead(self, data):
        newNode = Node(data)
        if len(self) == 0:
            self._head = newNode
        else:
            newNode._next = self._head
            self._head = newNode
        self._count += 1

    def insertAtTail(self, data):
        newNode = Node(data)
        current = self._head

        while current._next:
            current = current._next

        current._next = newNode
        self._count += 1

    def removeHead(self):
        if len(self) == 0:
            raise EmptyError('Empty linked list')
        else:
            result = self._head._data
            self._head = self._head._next
            self._count -= 1
        return result
        
    def removeTail(self):
        if len(self) == 0:
            raise EmptyError('Empty linked list')
        else:
            current = self._head
            previous = None
            if current._next:
                while current._next:
                    previous = current
                    current = current._next
                previous._next = None
                result = current._data  
            else:
                self._head = None
                result = current._data  
            self._count -= 1
            return result