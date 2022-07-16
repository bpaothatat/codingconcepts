from logging import root


class BinaryTree:
    def __init__(self, data) -> None:
        self._data = data
        self._left = None
        self._right = None

    def insert(self, data) -> None:
        if self._data:
            if data < self._data:
                if self._left is None:
                    self._left = BinaryTree(data)
                else:
                    self._left.insert(data)
            elif data > self._data:
                if self._right is None:
                    self._right = BinaryTree(data)
                else:
                    self._right.insert(data)
        else:
            self._data = data

    def in_order_traversal(self):
        items = []
        if self._left:
            items += self._left.in_order_traversal()
        items.append(self._data)
        if self._right:
            items += self._right.in_order_traversal()
        return items

def build_tree(data:list) -> BinaryTree:
    root = None
    if len(data) > 0:
        root = BinaryTree(data[0])
        for i in range(1, len(data)):
            root.insert(data[i]) 
    return root
