import unittest
from binarytree import *

class BinaryTreeTest(unittest.TestCase):

    def test_in_order_traversal(self):
        tree = build_tree([17, 4, 1, 1, 10])
        self.assertEqual(tree.in_order_traversal(), [1, 4, 10, 17])

    def test_pre_order_traversal(self):
        tree = build_tree([17, 4, 1, 1, 10])
        self.assertEqual(tree.pre_order_traversal(), [17, 4, 1, 10])

    def test_post_order_traversal(self):
        tree = build_tree([17, 4, 1, 1, 10])
        self.assertEqual(tree.post_order_traversal(), [1, 10, 4, 17])

    def test_min(self):
        tree = build_tree([3,1,10])
        self.assertEqual(tree.find_min(), 1)

    def test_max(self):
        tree = build_tree([3,1,10])
        self.assertEqual(tree.find_max(), 10)

    def test_search(self):
        tree = build_tree([17, 4, 1, 1, 10])
        self.assertEqual(tree.find(17).data, 17)
        self.assertEqual(tree.find(1).data, 1)
        self.assertEqual(tree.find(10).data, 10)
        self.assertEqual(tree.find(4).data, 4)
        self.assertEqual(tree.find(-1), None)

if __name__ == '__main__':
    unittest.main()