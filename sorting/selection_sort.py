from typing import List

def select(seq: List[int], start: int) -> int:
    """
    Find the index of the minimum element in the subarray seq[start:].

    Args:
        seq: A list of integers.
        start: An integer, the starting index of the subarray.

    Returns:
        An integer, the index of the minimum element in the subarray seq[start:].
    """
    # Initialize min_index as the starting index of the subarray
    min_index = start
    
    # Loop over the subarray and find the index of the minimum element
    for j in range(start + 1, len(seq)):
        if seq[min_index] > seq[j]:
            min_index = j
    
    # Return the index of the minimum element
    return min_index


def selection_sort(seq: List[int]) -> List[int]:
    """
    Sort the input list using selection sorting algorithm.

    Args:
        seq: A list of integers.

    Returns:
        A list of integers, sorted in ascending order.
    """
    n = len(seq)

    for i in range(n-1):
        # Find the index of the minimum element in the unsorted part of the list
        min_index = select(seq, i)
        
        # Swap the minimum element with the first element of the unsorted part of the list
        seq[i], seq[min_index] = seq[min_index], seq[i]
    
    return seq

seq = [5,8,2,6,9,1,0,7]
print(f'Before Selection sorting: {seq}')
sorted_seq = selection_sort(seq)
print(f'After Selection sorting: {sorted_seq}')
