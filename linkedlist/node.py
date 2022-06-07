class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def __str__(self):
        return str(self._data)