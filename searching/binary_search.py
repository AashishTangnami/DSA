

def binary_search_iterative(arr: list[int], x: int) -> int:
    """
    Performs binary search iteratively to find the index of x in arr.
    Returns -1 if x is not found in arr.
    """
    low, high = 0, len(arr) - 1 # initialize the indices of the lowest and highest elements in the array
    while low <= high:
        mid = (low + high) // 2 # find the middle index of the array
        if arr[mid] == x: # if the middle element is the target, return its index
            return mid
        elif arr[mid] < x: # if the middle element is less than the target, search the right half of the array
            low = mid + 1
        else: # if the middle element is greater than the target, search the left half of the array
            high = mid - 1
    return -1 # if the target is not found, return -1

def binary_search_recursive(arr: list[int], x: int) -> int:
    """
    Performs binary search recursively to find the index of x in arr.
    Returns -1 if x is not found in arr.
    """
    def binary_search_helper(arr: list[int], x: int, low: int, high: int) -> int:
        if high >= low:
            mid = (low + high) // 2 # find the middle index of the array
            if arr[mid] == x: # if the middle element is the target, return its index
                return mid
            elif arr[mid] > x: # if the middle element is greater than the target, search the left half of the array
                return binary_search_helper(arr, x, low, mid - 1)
            else: # if the middle element is less than the target, search the right half of the array
                return binary_search_helper(arr, x, mid + 1, high)
        else:
            return -1 # if the target is not found, return -1
    return binary_search_helper(arr, x, 0, len(arr) - 1)

def main(index_value: int, x: int, method: str) -> None:
    """
    Prints the result of the binary search for a given index_value, input value x, and method.
    """
    if index_value != -1:
        print(f"Position of the input value x: {x} is at: {index_value} using {method}")
    else:
        print(f"Position of the input value x: {x} is not found using {method}")

arr = [5, 8, 2, 6, 9, 1, 0, 7]
sorted_arr = sorted(arr) # sort the array to apply binary search
x = 6
index_value1 = binary_search_iterative(sorted_arr, x)
index_value2 = binary_search_recursive(sorted_arr, x)
main(index_value1, x, "binary search iterative")
main(index_value2, x, "binary search recursive")
