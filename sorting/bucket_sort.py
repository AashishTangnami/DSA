# Bucket sorting divides the unsorted array elements into several groups called buckets.
# Scatter gather approach is used  in the bucket sort process.
# complexity
    # best - O(n+k)
    # worst - O(n^2)
    # avg - O(n)
def bucket_sort(seq):
    bucket = []

    # Create empty buckets
    for i in range(len(seq)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in seq:
        idx_b = int(10 * j)
        bucket[idx_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(seq)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(seq)):
        for j in range(len(bucket[i])):
            seq[k] = bucket[i][j]
            k += 1
    return seq


seq = [.42, .32, .33, .52, .37, .47, .51]
print(f'Unsorted list : {seq}')
print(f"Sorted list in ascending order is : {bucket_sort(seq)}")
