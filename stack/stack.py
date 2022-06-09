from exceptions import EmptyError

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
