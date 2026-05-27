"""
    4.3 Write a recursive function to find the maximum number in a list.
"""

def max_number_item(arr : []):
    # base case 
    if arr and len(arr) <= 1:
        return arr[0] if arr[0] else 0
    else :
        # recursive case
        if arr[0] > max_number_item(arr[1:]):
            return arr[0]
        
        return max_number_item(arr[1:])


# arr = [1, 2, 3, 4, 5]
# arr = [10]
arr = [10, 2]


print(max_number_item(arr))

