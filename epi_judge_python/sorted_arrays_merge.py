from typing import List
import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # Each file is sorted in increasing order of time
    '''
    1) Parse a file
    2) Parse each file and load into a min heap
    3) Offload the min heap

    Approach 1: Pointer per file - load minimums onto a heap. If selected, advance pointer
    - initialize pointers & heap
    - load each minimum onto heap and advance pointers
    - pop the heap and advance list of chosen - if not at end of list append next item

    Heap item representation: (timestamp, file_id)

    Time Complexity: 
    Min-heap size stays at k files so the time complexity breaks down to:
    - O(k) to instantiate
    - O(n*log(k)) for the heap operations. N pushes to heap will happen with log(k) insertion
    Total time complexity is O(n*log(k)) with k<<n 
    '''
    heap = []
    result = []
    for file_id, timestamps in enumerate(sorted_arrays):
        index = 0
        if index == len(timestamps): # Exhausted this list
            continue
        time_to_add = timestamps[index]
        heapq.heappush(heap, (time_to_add, file_id, index))

    while len(heap) > 0:
        timestamp, origin, index = heapq.heappop(heap)
        # Add to result
        result.append(timestamp)
        # Advance pointer & optionall add item
        next_index_for_origin = index + 1
        if next_index_for_origin == len(sorted_arrays[origin]):
            continue # Nothing to add from this list
        # Push next item from origin into the heap
        time_to_push = sorted_arrays[origin][next_index_for_origin]
        heapq.heappush(heap, (time_to_push, origin, next_index_for_origin))
        

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
