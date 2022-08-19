# Bubble Sort
# Compares two adjacent elements and swaps them until they are in the intended order.
# Each element of the array move to the end in each iteration.

"""Pseudocode
1. Compare first and second index element.
2. If the first element is greater than the second, then swap element.
3. Now, compare second and third element, swap if they are unsorted.
4. Iterate the process untill last element.

"""
def bubble_sort(lst):
    # Access each element in the list
    for i in range(len(lst)):
        # compare elements in the list
        for j in range(0, len(lst)-i-1):
            # compare two adjacent elements.
            # change > to < to sort in descending order.
            if lst[j] > lst[j + 1]: # ascending order
                tmp_lst = lst[j]
                lst[j] = lst[j+1] # swapping elements
                lst[j+1] = tmp_lst 

    return lst


seq = [5,8,2,6,9,1,0,7]
print(f'Before bubble sorting: {seq}')
sorted_seq = bubble_sort(seq)
print(f'After bubble sorting: {sorted_seq}')
