from typing import List

def bucket_sort(seq: List[float]) -> List[float]:
    """
    Sorts a list of floats using the Bucket Sort algorithm.
    
    complexity
        best - O(n+k)
        worst - O(n^2)
        avg - O(n)
    """
    n = len(seq)
    # Create empty buckets
    bucket = [[] for _ in range(n)]

    # Insert elements into their respective buckets
    for j in seq:
        idx_b = int(n * j)
        bucket[idx_b].append(j)

    # Sort the elements of each bucket
    for i in range(n):
        bucket[i].sort()

    # Get the sorted elements
    sorted_seq = [elem for bucket_list in bucket for elem in bucket_list]

    return sorted_seq

# Example usage
seq = [.42, .32, .33, .52, .37, .47, .51]
print(f'Unsorted list : {seq}')
print(f"Sorted list in ascending order is : {bucket_sort(seq)}")
