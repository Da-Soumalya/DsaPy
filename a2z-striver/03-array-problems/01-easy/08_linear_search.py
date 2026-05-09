def linear_search(arr, key):
    for ind, val in enumerate(arr):
        if val == key:
            return ind
    return -1


arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 5),
      linear_search(arr, 6))