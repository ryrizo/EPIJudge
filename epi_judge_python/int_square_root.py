from test_framework import generic_test


def square_root(k: int) -> int:
    left, right = 0, 1
    while right**2 < k:
        left = right
        right *= 2

    greatest_seen = left
    while left <= right:
        middle = (right - left) // 2 + left
        if middle**2 <= k: # middle works
            greatest_seen = middle
            left = middle + 1
        else: # Middle is too large
            right = middle - 1
    
    return greatest_seen


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
