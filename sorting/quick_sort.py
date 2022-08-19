# Quick sort algorithm is also based on divide and conquer approach
# Array - divided into subarrays by selecting a pivot element.
# pivot element divides the actual array.
# all the smaller elements are indexed before pivot and greater elements are indexed after pivot element.
# left and right elements are again divided with the same pivot approach.
# with sorted sub-arrays, combining them all again and create a sorted array with quick sort algorithm.

import random

def partition(seq, start, stop):
    start = None
    stop = None
    return seq

def quick_sort(seq):
    return seq


seq = [5,8,2,6,9,1,0,7]
print(f'Before Selection sorting: {seq}')
sorted_seq = quick_sort(seq)
print(f'After Selection sorting: {sorted_seq}')