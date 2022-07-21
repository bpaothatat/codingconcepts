import unittest
from binarytree import BinaryTree, build_tree

class BinaryTreeTest(unittest.TestCase):

    def test_in_order_traversal(self):
        tree = build_tree([17, 4, 1, 1, 10])
        self.assertEqual(tree.in_order_traversal(), [1, 4, 10, 17])

    def test_min(self):
        tree = build_tree([3,1,10])
        self.assertEqual(tree.find_min(), 1)

    def test_max(self):
        tree = build_tree([3,1,10])
        self.assertEqual(tree.find_max(), 10)

    def test_search(self):
        tree = build_tree([17, 4, 1, 1, 10])
        self.assertTrue(tree.search(17))
        self.assertTrue(tree.search(1))
        self.assertTrue(tree.search(10))
        self.assertTrue(tree.search(4))
        self.assertFalse(tree.search(-1))

if __name__ == '__main__':
    unittest.main()