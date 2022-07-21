class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data) -> None:
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current:Node):
        if current.data > data:
            if current.left == None:
                new_node = Node(data)
                new_node.parent = current
                current.left = new_node
            else:
                self._insert(data, current.left)
        elif current.data < data:
            if current.right == None:
                new_node = Node(data)
                new_node.parent = current
                current.right = new_node
            else:
                self._insert(data, current.right)

    def find(self, data) -> Node:
        if self.root == None:
            return None
        return self._find(data, self.root)

    def _find(self, data, current:Node):
        if current.data == data:
            return current
        elif current.data > data and current.left:
            return self._find(data, current.left)
        elif current.data < data and current.right:
            return self._find(data, current.right)
        return None

    def in_order_traversal(self):
        items = []
        self._in_order_traversal(items, self.root)
        return items
    
    def _in_order_traversal(self, items, current:Node):
        if current.left:
            self._in_order_traversal(items, current.left)
        items.append(current.data)
        if current.right:
            self._in_order_traversal(items, current.right)

    def find_min(self):
        if self.root == None:
            return None
        return self._find_min(self.root)

    def _find_min(self, current:Node):
        if current.left == None:
            return current.data
        return self._find_min(current.left)
          
    def find_max(self):
        if self.root == None:
            return None
        return self._find_max(self.root)
    
    def _find_max(self, current:Node):
        if current.right == None:
            return current.data
        return self._find_max(current.right)

def build_tree(data:list) -> BinaryTree:
    tree = BinaryTree()
    for item in data:
        tree.insert(item)
    return tree
