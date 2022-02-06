from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    if tree is None:
        return None
    # Approach: Store lowest greater than, choose next node until end
    if tree.data > k: # Record and go left
        closer_option = find_first_greater_than_k(tree.left, k)
        return closer_option if closer_option else tree
    else: # Less than equals go right
        return find_first_greater_than_k(tree.right, k) 



def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
