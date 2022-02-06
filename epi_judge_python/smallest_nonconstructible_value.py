from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    seen_sum = set()
    A.sort()
    if A[0] > 1:
        return 1

    target = 1
    for item in A:
        sums_to_add = [item + i for i in seen_sum]
        while sums_to_add:
            seen_sum.add(sums_to_add.pop())
        seen_sum.add(item)
        if target not in seen_sum:
            return target
        target += 1

    while target in seen_sum:
        target += 1
    return target


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
