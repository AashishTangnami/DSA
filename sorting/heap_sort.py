# Heap Sort in python

def heap(seq, n, i):
    large_val = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and seq[i] < seq[left]:
        large_val = left
  
    if right < n and seq[large_val] < seq[right]:
        large_val = right

    # If root is not largest, swap with largest and continue heapifying
    if large_val != i:
        seq[i], seq[large_val] = seq[large_val], seq[i]
        heap(seq, n, large_val)

def heap_sort(seq):
    n = len(seq)
    for i in range(n//2, -1, -1):
        heap(seq, n, i)
    
    for i in range(n-1, 0, -1):
        # Swap
        seq[i], seq[0] = seq[0], seq[i]
  
        # Heapify root element
        heap(seq, i, 0)

seq = [5, 8, 2, 6, 9, 1, 0, 7]
heap_sort(seq)
n = len(seq)
print("Sorted array is")
for i in range(n):
    print("%d " % seq[i], end='')
  