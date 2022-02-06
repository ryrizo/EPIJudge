from typing import List

from test_framework import generic_test

'''
Tricky summation to get right. 
'''
def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times.sort()
    collected_waiting_time = 0 
    for i, choice in enumerate(service_times):
        collected_waiting_time += (choice * (len(service_times) - (i+1)))
    return collected_waiting_time


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
