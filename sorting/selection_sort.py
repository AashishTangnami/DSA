# selection sorting 
# select the smallest element from an unsorted list in each iteration.
# place the smallest element at the begining of the unsorted list.

""" Pseudocode
1. compare minimum with second element.
2. If the second element is smaller than first element, assign second element as minimum
3. Compare minimum with third element as so on, iterate the process till the last element.
4. After each iteration, minimum is placed in the front of the unsorted list.
"""

def select(seq: list, start: int)-> int:
    
    min_index = start
    for j in range(start + 1, len(seq)):
        if seq[min_index] > seq[j]:
            min_index = j
    return min_index

def selection_sorting(seq: list)->list:
    for i in range(len(seq)-1):
        min_index = select(seq, i)
        tmp_idx = seq[i]
        seq[i] = seq[min_index]
        seq[min_index] = tmp_idx
    return seq

seq = [5,8,2,6,9,1,0,7]
print(f'Before Selection sorting: {seq}')
sorted_seq = selection_sorting(seq)
print(f'After Selection sorting: {sorted_seq}')
