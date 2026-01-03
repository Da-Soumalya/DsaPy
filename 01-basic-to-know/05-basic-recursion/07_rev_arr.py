'''
# this will be the non-recursive(iterative) variant

def rev_array(arr):
    l = len(arr)
    j = l-1
    for i in range(l):
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        j -= 1
    return arr
'''


def rev_array(arr, start, end):
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return rev_array(arr, start+1, end-1)


def main():
    arr = [1, 2, 3, 4, 5]
    print(rev_array(arr, 0, len(arr)-1))