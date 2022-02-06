from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    """
    A is sorted and contains enough empty entries at the end to contain B
    A needs to be returned as fully sorted
    m is the number of non-empty entries in A - representation could be a zero to denote empty
    n is number of entries in B.
    """
    # Brute force
    a_marker = 0
    last_meaningful_entry_in_a = m - 1
    for b in B:
        for i, a in enumerate(A[a_marker:last_meaningful_entry_in_a + 1]):
            if b <= a:
                a_marker = a_marker + i
                A.insert(a_marker, b)
                last_meaningful_entry_in_a += 1
                A.pop(len(A)-1)
                break  # No need to continue search for this b

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
