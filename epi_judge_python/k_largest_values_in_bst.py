from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    ''' Approach: populate right, self, left until result satisfied
    
    '''
    return find_k_helper(tree, k, [])

def find_k_helper(tree, k, result) -> List[int]:
    if tree is None or len(result) >= k:
        return result

    # Let right append first
    result = find_k_helper(tree.right, k, result)
    
    # I append second
    if len(result) == k: 
        return result
    result.append(tree.data)
    
    # Left appends last
    return find_k_helper(tree.left, k, result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
