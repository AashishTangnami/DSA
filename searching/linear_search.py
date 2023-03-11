from typing import List

def linear_search(arr: List[int], n: int, x: int) -> int:
    """
    Perform linear search to find the index of x in arr.

    Args:
        arr: A list of integers to be searched.
        n: An integer, the size of the list arr.
        x: An integer, the value to be searched for.

    Returns:
        An integer, the index of x in arr, or -1 if x is not found.
    """
    # Loop through the list and check each element for a match with x
    for i in range(0, n):
        if arr[i] == x:
            # If a match is found, return the index
            return i
    
    # If no match is found, return -1
    return -1

# Example usage
arr = [5, 8, 2, 6, 9, 1, 0, 7]
x = 0
n = len(arr)

# Perform linear search to find the index of x in arr
idx = linear_search(arr, n, x)

# Check the result and print a message accordingly
if idx == -1:
    print(f"The element {x} is not in the arr")
else:
    print(f"Element {x} is at index {idx}")
