from typing import List
import bisect

from test_framework import generic_test

def search_first_of_k(A: List[int], k: int) -> int:
    left, right = 0, len(A) - 1
    lowest_index = -1
    while left <= right:
        middle = (right - left) // 2 + left 
        if A[middle] >= k: # Mark and search left
            if A[middle] == k:
                lowest_index = middle
            right = middle - 1
        else: # search right - middle value less than k
            left = middle + 1
    return lowest_index


def search_first_of_k_using_library(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    first_biggger_or_equal_k = bisect.bisect_left(A, k)
    if first_biggger_or_equal_k >= len(A) or A[first_biggger_or_equal_k] != k:
        return -1
    return first_biggger_or_equal_k


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
