def right_rotate_by_one(arr):
    if arr:
        last = arr.pop()      
        arr.insert(0, last) 
    return arr


arr = [1, 2, 3, 4, 5]
print(right_rotate_by_one(arr))  