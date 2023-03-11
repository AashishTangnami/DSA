from typing import List

def merge(seq: List[int], start: int, mid: int, stop: int) -> None:
    """
    Merge two sorted sub-sequences into one sorted sequence.
    """
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

def merge_sort_recursively(seq: List[int], start: int, stop: int) -> List[int]:
    """
    Recursively sort the sequence by dividing it into smaller sub-sequences
    until the sub-sequence is only one element, then merging them back into a
    sorted sequence.
    """
    if start >= stop - 1:
        return seq
    mid = (start + stop) // 2
    merge_sort_recursively(seq, start, mid)
    merge_sort_recursively(seq, mid, stop)
    merge(seq, start, mid, stop)
    return seq

def merge_sort(seq: List[int]) -> List[int]:
    """
    Sort a sequence in non-descending order using merge sort.
    """
    return merge_sort_recursively(seq, 0, len(seq))


# Example usage
seq = [5, 8, 2, 6, 9, 1, 0, 7]
print("Original sequence:", seq)
sorted_list = merge_sort(seq)
print("Sorted sequence:", sorted_list)
