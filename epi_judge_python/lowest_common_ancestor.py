import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import namedtuple

CountWithLCA = namedtuple('CountWithLCA', ('counts', 'lca'))



def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        return lca_helper(tree, node0, node1).lca or tree

def lca_helper(node, node0, node1) -> CountWithLCA:
    if node is None:
        return CountWithLCA(counts=0, lca=None)

    left_count = lca_helper(node.left, node0, node1)
    if left_count.counts == 2:
        return left_count
    right_count = lca_helper(node.right, node0, node1)
    if right_count.counts == 2:
        return right_count

    num_here = (node0, node1).count(node)
    counts_here = right_count.counts + left_count.counts + num_here
    lca_found = node if counts_here == 2 else None 
    return CountWithLCA(counts=counts_here, lca=lca_found)



@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
