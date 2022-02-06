from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from collections import namedtuple

NodeAndCounts = namedtuple('NodeAndCounts', ('node', 'counts'))


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    # TODO - you fill in here.
    node_and_counts = bst_rebuild_helper(preorder_sequence, float('-inf'), float('inf'))
    return node_and_counts.node

def bst_rebuild_helper(sequence, floor, ceil) -> NodeAndCounts:
    if len(sequence) == 0: # Nothing left to do
        return NodeAndCounts(node=None, counts=0)

    node = BstNode(data=sequence[0])
    if not(floor < node.data < ceil):
        # This node belongs to someone else
        return NodeAndCounts(node=None, counts=0)

    # Node is in proper range
    node_counts = 1

    # Build left if we should
    next_node = sequence[node_counts] if len(sequence) > node_counts else None
    if next_node and next_node < node.data: # Build left - next node smaller
        left = bst_rebuild_helper(sequence[node_counts:], floor, node.data)
        node_counts += left.counts
        node.left = left.node

    # Build right if we should
    next_node = sequence[node_counts] if len(sequence) > node_counts else None
    if next_node and next_node > node.data: # Build right - next node bigger
        right = bst_rebuild_helper(sequence[node_counts:], node.data, ceil)
        node_counts += right.counts
        node.right = right.node

    return NodeAndCounts(node=node, counts=node_counts)




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
