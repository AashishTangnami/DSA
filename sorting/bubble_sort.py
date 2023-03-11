from typing import List

def bubble_sort(lst: List[int]) -> List[int]:
    """Sorts a list of integers in ascending order using bubble sort algorithm.
    
    Args:
        lst: A list of integers to be sorted.
    
    Returns:
        A sorted list of integers.
    """
    
    # Access each element in the list
    for i in range(len(lst)):  # O(n)
        # compare elements in the list
        for j in range(0, len(lst)-i-1):  # O(n)
            # compare two adjacent elements.
            # change > to < to sort in descending order.
            if lst[j] > lst[j + 1]:  # O(1)
                # swapping elements
                lst[j], lst[j+1] = lst[j+1], lst[j]  # O(1)

    return lst

seq = [5,8,2,6,9,1,0,7]
print(f'Before bubble sorting: {seq}')  # O(1)
sorted_seq = bubble_sort(seq)
print(f'After bubble sorting: {sorted_seq}')  # O(1)
