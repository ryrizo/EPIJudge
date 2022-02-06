import functools
import math
import heapq
import itertools
from typing import Iterator, List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    # Approach 1: Add all of the star to a min heap and pop 10 - Crazy number of stars though
    # Approach 2: Use a max heap, to store smallest seen values - remove max if something smaller seen
    # Time Complexity: Iterate all of the stars, N, inserting at worse N stars into a heap with max k items
    # O(n*log(k)) - which is much better than n*log(n) with a min heap
    # Simplification available is to push each time and pop each time its bigger than k. 
    
    # Heap representation (-1*distance, star)
    heap = [] # To make this a max heap, I need to give it a negative distance key
    result = []
    # Add first K 
    for star in itertools.islice(stars, k):
        heapq.heappush(heap, (-1 * star.distance, star)) 

    # Iterate remaining stars
    for candidate_star in stars:
        # If distance is less than max heap element, push this star and remove old star
        candidate_distance = candidate_star.distance
        if heap[0][1].distance >= candidate_distance:
            # The furthest seen close star is further than this one - remove max and add this smaller one
            heapq.heappushpop(heap, (-1 * candidate_distance, candidate_star))

    # Drain the heap for result
    while len(heap) > 0:
        result.append(heapq.heappop(heap)[1])
    return result


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
