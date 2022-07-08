class BinaryTree:
    def __init__(self, data) -> None:
        self._data = data
        self._left = None
        self._right = None

    def insert(self, data) -> None:
        if self.data:
            if data < self.data:
                if self._left is None:
                    self._left = BinaryTree(data)
                else:
                    self._left.insert(data)
            elif data > self.data:
                if self._right is None:
                    self._right = BinaryTree(data)
                else:
                    self._right.insert(data)
        else:
            self.data = data