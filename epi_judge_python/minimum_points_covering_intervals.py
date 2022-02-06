import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

def find_minimum_visits(intervals: List[Interval]) -> int:
    intervals.sort(key=lambda x: x[1])
    last_visited = float('-inf')
    num_visits = 0
    for interval in intervals:
        # If start is before last visit, skip. Else, visit end.
        if interval.left <= last_visited:
            continue # Skip - accounted for
        else: 
            last_visited = interval.right
            num_visits += 1
    return num_visits

'''
Right approach to pick the first end. You can track last visited time and count
to know if you should skip the next end or not. 
'''
def find_minimum_visits_first_go(intervals: List[Interval]) -> int:
    # Pick first end, remove intervales with start before end.
    intervals = sorted(intervals, key=lambda x: x[1]) # Sorted by end
    picks = find_minimum_visits_helper(intervals)
    return len(picks)

def find_minimum_visits_helper(intervals):
    if len(intervals) == 0:
        return [] # No more picks
    pick = intervals[0].right
    remaining_intervals = []
    for interval in intervals[1:]:
        if interval.left <= pick and interval.right >= pick:
            continue # Overlap is accounted for
        remaining_intervals.append(interval)
    future_picks = find_minimum_visits_helper(remaining_intervals)
    return [pick] + future_picks


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_points_covering_intervals.py',
            'minimum_points_covering_intervals.tsv',
            find_minimum_visits_wrapper))
