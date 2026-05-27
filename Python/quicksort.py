"""
    QUICKSORT
"""
import random


def quicksort(arr, low=0, high=None):
    if not arr:
        return []
    if len(arr) == 1:
        return arr
    
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr
        else:
            arr[0], arr[1] = arr[1], arr[0]
            return arr

    high = len(arr) - 1
    pivot = random.randrange(low, high)
    low_partition = [i for i in arr if i < arr[pivot]]
    high_partition = [i for i in arr if i > arr[pivot]]

    return quicksort(low_partition) + [arr[pivot]] + quicksort(high_partition)
    
# arr = [23]
# arr = [2, 3]
arr = [3, 3, 2, 2, 1]
# arr = [3, 1, 4, 2, 0]

print(quicksort(arr))
