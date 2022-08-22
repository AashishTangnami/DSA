# Linear search algorithm is a sequential searching algorithm.
# Start from the first element, compare k(input_value) with each element x in the existing array/list.
# If k == x, then return the index.
# else not found.
# complexity - O(n) -> directly proportional to the size of the array/list.


def linear_search(arr, n, x):
    for i in range(0, n):
        if(arr[i] == x):
            return i
    return -1

arr = [5,8,2,6,9,1,0,7]
x = 0
n = len(arr)

sorted_arr = linear_search(arr, n ,x)
if(sorted_arr == -1):
    print(f'The element {x} is not in the arr')
else:
    print(f'Element is at index: {sorted_arr}')
