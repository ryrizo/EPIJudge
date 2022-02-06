import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))

def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    task_durations.sort() # O(nlogn)
    return [
        PairedTasks(task_durations[i], task_durations[~i])
        for i in range(len(task_durations)//2)
    ]


''' Find median required sorting at O(nlogn) - if sorting its easier.
If sorting a much easier greedy approach is available
'''
def optimum_task_assignment_first_go(task_durations: List[int]) -> List[PairedTasks]:
    median = find_median(task_durations)
    above, below, medians = [], [], []
    for duration in task_durations:
        if duration > median:
            above.append(duration)
        elif duration < median:
            below.append(duration)
        else:
            medians.append(duration)
    while len(medians) > 0:
        if len(above) > len(below):
            below.append(medians.pop())
        else:
            above.append(medians.pop())
    return [(a, b) for a, b in zip(above, below)]

def find_median(durations):
    durations.sort()
    mid = int(len(durations)/2)
    middle1, middle2 = durations[mid], durations[mid - 1]
    return (middle1 + middle2) / 2

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
