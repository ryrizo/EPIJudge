from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    floor, ceiling = float('-inf'), float('inf')
    return bst_check_helper(tree, floor, ceiling)

def bst_check_helper(tree, floor, ceiling) -> bool:
    if tree is None:
        return True
    # Check here
    if not(floor <= tree.data <= ceiling): 
        return False 
    return bst_check_helper(tree.left, floor, tree.data) and \
         bst_check_helper(tree.right, tree.data, ceiling)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
