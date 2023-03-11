from typing import List

def heapify(seq: List[int], n: int, i: int) -> None:
    """
    Heapify the subtree rooted at index i in seq.

    Args:
    - seq: List of integers to be sorted
    - n: Size of the heap
    - i: Index of the subtree to be heapified
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # If left child is larger than root
    if left < n and seq[largest] < seq[left]:
        largest = left

    # If right child is larger than largest so far
    if right < n and seq[largest] < seq[right]:
        largest = right

    # If largest is not root
    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]  # swap
        heapify(seq, n, largest)

def heap_sort(seq: List[int]) -> List[int]:
    """
    Sort the given list of integers using heap sort algorithm.

    Args:
    - seq: List of integers to be sorted

    Returns:
    - Sorted list of integers
    """
    n = len(seq)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(seq, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        seq[i], seq[0] = seq[0], seq[i]  # swap
        heapify(seq, i, 0)

    return seq

seq = [5, 8, 2, 6, 9, 1, 0, 7]
print(f"Unsorted list: {seq}")
sorted_seq = heap_sort(seq)
print(f"Sorted list: {sorted_seq}")
