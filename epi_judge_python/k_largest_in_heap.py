from typing import List
import heapq

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    # Approach: Have a max-heap for adding layers of the heap to until k
    '''
    My approach of adding layer by layer was wrong. In a heap the values under the parent are ensured,
    not cousin relationships. 

    Need an exploration heap to do sort of a DFS by size: Heap repr (-value, i)
    1) Add root to heap
    2) Pop heap and add to result
    3) Add each child to heap 

    Time Complexity:
    k heap pushes of log k - max size of heap is k
    O(k*log(k))
    '''
    heap = [] # This needs to be a max heap representation (-value, value)
    result = []
    heapq.heappush(heap, (-A[0], 0))
    while len(result) < k:
        value, index = heapq.heappop(heap)
        result.append(-value)
        # Put children on exploration heap if not out of bounds
        for child in [2*index + 1, 2*index +2]:
            if child < len(A):
                heapq.heappush(heap, (-A[child], child))

    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
