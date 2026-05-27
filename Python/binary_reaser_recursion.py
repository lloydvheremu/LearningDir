"""
    Binary Search - Divide and Conquer
"""


def binary_search(arr: [], item):
    if not arr:
        return False
    midpoint = len(arr) // 2
    if item == arr[midpoint]:
        return True 
    elif item > arr[midpoint]:
        return binary_search(arr[midpoint + 1:], item)
    else :
        return binary_search(arr[:midpoint], item)
        



# arr = [1]
# arr = [1, 2, 3]
arr = [1, 2, 3, 4, 5, 6, 7]


print(binary_search(arr, 6))


