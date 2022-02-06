from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    citations.sort()
    h = 0
    for i in range(len(citations)):
        if citations[~i] < i + 1:
            return h
        h += 1
    return h


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
