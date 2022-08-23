# Quick sort algorithm is also based on divide and conquer approach
# Array - divided into subarrays by selecting a pivot element.
# pivot element divides the actual array.
# all the smaller elements are indexed before pivot and greater elements are indexed after pivot element.
# left and right elements are again divided with the same pivot approach.
# with sorted sub-arrays, combining them all again and create a sorted array with quick sort algorithm.
# complexity
    # O(n*log n) -> when pivot element is near to the middle.
import random

def partition(seq, start, stop):
    pivot = seq[stop]
    
    i = start - 1
    
    for j in range(start, stop):
        if seq[j] <= pivot:
            i = i + 1
            seq[i], seq[j] = seq[j], seq[i]
    seq[i + 1], seq[stop] = seq[stop], seq[i]
    return i + 1


def quick_sort_recursively(seq, start, stop):
    if start < stop:
        pivot = partition(seq, start, stop)
        print(pivot)
        quick_sort_recursively(seq, start, pivot - 1)
        quick_sort_recursively(seq, pivot +1, stop)
    return seq
def quick_sort(seq):
    start = 0
    stop = len(seq)
    quick_sort_recursively(seq, start, stop-1)
    return seq

seq = [5,8,2,6,9,1,0,7]
print(f'Before Selection sorting: {seq}')
sorted_seq = quick_sort(seq)
print(f'After Selection sorting: {sorted_seq}')