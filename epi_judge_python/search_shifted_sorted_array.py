from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    left, right = 0, len(A) - 1

    while left <= right:
        m = (right - left) // 2 + left
        if A[m - 1] > A[m]:
            return m # Found the drop point
        elif (m + 1 < len(A) and A[m+1] < A[m]):
            return m + 1 # Dop point could be on either side of m
        if A[left] <= A[m]: # Drop point is right 
            left = m + 1
        else: # Drop point is left
            right = m - 1
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
