from typing import List

def partition(seq: List[int], start: int, stop: int) -> int:
    """Select a pivot and move all elements less than the pivot to the left, 
        and all elements greater than the pivot to the right.
        Time Complexity: O(n)
    """
    pivot = seq[stop]
    i = start - 1
    
    for j in range(start, stop):
        # If element is less than or equal to pivot, move it to the left
        if seq[j] <= pivot:
            i = i + 1
            seq[i], seq[j] = seq[j], seq[i]
    
    # Move pivot to its final position
    seq[i + 1], seq[stop] = seq[stop], seq[i+1]
    return i + 1


def quick_sort_recursively(seq: List[int], start: int, stop: int) -> List[int]:
    """Recursively sort a list using the quicksort algorithm.
        Time Complexity: O(n*log(n)) average case, O(n^2) worst case
    
    """
    if start < stop:
        pivot = partition(seq, start, stop)
        quick_sort_recursively(seq, start, pivot - 1)
        quick_sort_recursively(seq, pivot +1, stop)
    return seq
    
def quick_sort(seq: List[int]) -> List[int]:
    """Sort a list using the quicksort algorithm.
        Time Complexity: O(n*log(n)) average case, O(n^2) worst case
    """
    start = 0
    stop = len(seq)
    quick_sort_recursively(seq, start, stop-1)
    return seq

seq = [5,8,2,6,9,1,0,7]
print(f'Before Quick sorting: {seq}')
sorted_seq = quick_sort(seq)
print(f'After Quick sorting: {sorted_seq}')
