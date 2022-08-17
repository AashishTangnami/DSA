# selection sorting 

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
