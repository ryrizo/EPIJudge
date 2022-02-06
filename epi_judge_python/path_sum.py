from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    return path_sum_helper(tree, remaining_weight, 0)

def path_sum_helper(node, target, running_sum):
    if node is None:
        return False

    weight = running_sum + node.data
    if node.left is None and node.right is None: # Leaf node
        return weight == target

    left_has_it = path_sum_helper(node.left, target, weight)
    if left_has_it:
        return True
    right_has_it = path_sum_helper(node.right, target, weight)
    if right_has_it:
        return True
    return False



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
