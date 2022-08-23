# Binary search algorithm is for searching an element's position in a sorted list/array.
# Binary search algorithm is implemented only in sorted array/list.

# Binary search algorithm implemented in two ways.
    # Iterative Method 
    # Recursive Method - divide and conquer approach

# Pseudocode
    # Set two high and low pointers as last and first element respectively.
    # Find the mid element of the list.
    # If the x(input) == mid then return mid, else compare again.
    # if the x > mid, compare elements between mid and high in the array.
    # repeat until low meets high.

# Itereative Method.
def binary_search_iterative(arr, x, low, high):
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# recursive method.
def binary_search_recursively(arr, x , low, high):
    if high >= low:
        mid = low + (high - low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursively(arr, x , low, mid-1)
        else:
            return binary_search_recursively(arr, x, mid+1, high)
    else:
        return -1

def main(index_value, str):
    print(str)
    if index_value != -1:
        print(f'Position of the input value x : {x} is at : {index_value}')
    else:
        print(f'Position of the input value x : {x} is not found')


arr = [5,8,2,6,9,1,0,7]
sorted_arr = sorted(arr)
x = 6
low = sorted_arr[0]
high = sorted_arr[-1]
index_value1 = binary_search_iterative(sorted_arr, x, low, high)
index_value2 = binary_search_recursively(sorted_arr, x , low, high)
main(index_value1, 'Binary Search iterative method')
main(index_value2, 'Binary Search recursive method')