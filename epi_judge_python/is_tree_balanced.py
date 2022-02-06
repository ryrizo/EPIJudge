from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import Tuple
from collections import namedtuple

BalancedWithHeight = namedtuple('BalancedWithHeight', ('is_balanced', 'height'))


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    balance_with_height = tree_height(tree)
    return balance_with_height.is_balanced

def tree_height(node) -> Tuple[int, bool]: 
    if node is None: # A leaf node got us here
        return BalancedWithHeight(is_balanced=True, height=0)

    left = tree_height(node.left)
    if not left.is_balanced:
        return BalancedWithHeight(is_balanced=False, height=-1)

    right = tree_height(node.right)
    if not right.is_balanced:
        return BalancedWithHeight(is_balanced=False, height=-1)

    this_height = max(left.height, right.height) + 1
    is_balanced = abs(left.height - right.height) <= 1
    return BalancedWithHeight(is_balanced=is_balanced, height=this_height)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
