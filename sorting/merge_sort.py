# Merge Sorting Algorithm is based on the principle of Divide and Conquer Algorithm
# Divide and Conquer Algo.
    # 1. Divide: Divide the given problem into sub-problems using recursion.
    # 2. Conquer: Solve the smaller sub-problem using recursion, if the problem is small do it directly.
    # 3. Combine: Combine the solutions of the sub-problem that are part of the recursive process to solve the actual problem.
"""Pseudocode
1. Create copies of the sub-arrays - start, mid, and stop.
2. Create three pointers i, j, and k
    - i is for the current index of start, starting at 1
    - j is for the current index of mid, starting at 1
    - k is for the current index for combining start and mid in new list at some starting point.
3. Iterate untill end of the start or mid, pick the larger among the elements form start and mid, then index them in the correct position in new list.
4. Iterate through remaining elements and put them in the correspoding index in new list.
"""
# Complexity
    # Best O(n*log*n)
    # space complexity - O(n) 
def merge(seq, start, mid, stop):
    tmp_list = []
    i = start
    j = mid

    # Merge the two lists while each has more elements
    while i < mid and j < stop:
        if seq[i] < seq[j]:
            tmp_list.append(seq[i])
            i += 1
        else:
            tmp_list.append(seq[j])
            j += 1
    # copy in the rest of the start to mid sequence.
    while i < mid:
        tmp_list.append(seq[i])
        i += 1

    for i in range(len(tmp_list)):
        seq[start + i] = tmp_list[i]

def merge_sort_recursively(seq, start, stop):
    
    if start >= stop - 1:
        return
    mid = (start + stop) // 2

    merge_sort_recursively(seq, start, mid)
    merge_sort_recursively(seq, mid, stop)
    merge(seq, start, mid, stop)
    return seq

def merge_sort(seq):
    return merge_sort_recursively(seq, 0, len(seq))


seq = [5,8,2,6,9,1,0,7]
print(seq)
sorted_list = merge_sort(seq)
print(sorted_list)
