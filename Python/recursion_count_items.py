# couunt number of items in a list

def count_recursively(arr: []):
    # base case
    if len(arr) <= 1:
        return 1 if len(arr) == 1 else 0

    # recursive case
    count = 0
    return 1 + count_recursively(arr[1:])



myarr = [1, 2, 3, 4, 5]


print(count_recursively(myarr))
