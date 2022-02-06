from typing import Iterator, List
import heapq
from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    '''
    When I see an element, I need to see k more elements to know if its sorted properly

    Approach: Have a tiny min heap to help
    - Load first k elements from the sequence into the heap
    - For all remaining elements do a push pop of the heap to get what should be added
    - Drain the remaining heap

    Time Complexity:
    O(n*log(k)) - each item n will be pushed onto a heap with max size k
    '''
    result = []
    heap = []

    next_element = next(sequence, None)
    while next_element is not None:
        heapq.heappush(heap, next_element)
        if len(heap) > k: # Have enough information to add to result
            result.append(heapq.heappop(heap))
        next_element = next(sequence, None)

    # Drain remaining
    while len(heap) > 0:
        result.append(heapq.heappop(heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
