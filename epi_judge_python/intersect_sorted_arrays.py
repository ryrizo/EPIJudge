from typing import List, Optional

from test_framework import generic_test

def intersect_two_sorted_arrays(A, B):
    result = []
    ai, bi = 0, 0
    while ai < len(A) and bi < len(B): # While array not exhausted
        if A[ai] == B[bi]:
            result.append(A[ai])
            ai = advance_index(A, ai)
            bi = advance_index(B, bi)
        elif A[ai] < B[bi]:
            ai += 1
        else: # B value less than A value
            bi += 1
    return result

def advance_index(array, index) -> int:
    new_index = index
    while new_index < len(array) and array[new_index] == array[index]:
        new_index += 1
    return new_index

def intersect_two_sorted_arrays_one_line(A, B):
    return sorted(list(set(A) & set(B)))

# There is a way to get this down to O(m+n), but good job.
def intersect_two_sorted_arrays_first_go(A: List[int], B: List[int]) -> List[int]:
    # Intersection is ordered, without duplicates
    # Brute force
    intersection = []  # Any consequences to using set here? What if I did set(A)?
    # for doc_id in A:  # This will be n even if I remove the duplicates
    #     if doc_id in B:  # Expected complexity for search of an array O(n), I can do O(log(n))
    #         if len(intersection) > 0 and intersection[-1] == doc_id:
    #             continue  # Eliminates duplicates
    #         intersection.append(doc_id)

    ### O(n*log(m)) NOTE: the bigger array should be passed to the log(m) complexity function
    if len(A) >= len(B):
        search_target, query_docs = A, B
    else:
        search_target, query_docs = B, A

    for doc_id in query_docs:
        if search_array_for_element(search_target, doc_id):
            if len(intersection) > 0 and intersection[-1] == doc_id:
                continue  # Skip duplicates
            intersection.append(doc_id)

    return intersection


def search_array_for_element(array, value) -> bool:
    """

    :param array: ordered array to look for an element
    :param value:
    :return: Optional index of b if found.
    """
    if len(array) == 0 or value > array[-1]:
        # Early terminate for ordered.
        return False

    if len(array) == 1:
        return array[0] == value

    middle_index = int(len(array) / 2)
    middle_value = array[middle_index]
    if middle_value == value:
        return True
    elif middle_value > value:
        # Search left side
        return search_array_for_element(array[:middle_index], value)
    else:
        # Search right side
        return search_array_for_element(array[middle_index:], value)


def test_recursive_search():
    cases = [
        ([1], 1, True),
        ([2, 3], 2, True),
        ([2], 3, False),
        ([1, 2, 3], 3, True)
    ]
    for array, doc_id, expectation in cases:
        print(f"Attempting case: {array}")
        assert search_array_for_element(array, doc_id) == expectation


if __name__ == '__main__':
    # test_recursive_search()
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
