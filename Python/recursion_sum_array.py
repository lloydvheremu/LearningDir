# Given an array myarr = [2, 4, 6]
# Create a recursive function to sum any array of any size


def sum_recursively(arr: []):
    # base case len <= 1
    if len(arr) <= 1:
        return arr[0] if arr[0] else 0
    else:
        return arr[0] + sum_recursively(arr[1:])

myarr = [2, 4, 6, 12]

print(sum_recursively(myarr))



