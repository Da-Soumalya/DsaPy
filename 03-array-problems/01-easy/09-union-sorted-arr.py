'''
Input: n = 10, m = 7, arr1[] = {1,2,3,4,5,6,7,8,9,10} arr2[] = {2,3,4,4,5,11,12}
'''

def union_sorted(arr1, arr2):
    arr = [float('inf')]
    i , j, prev = 0, 0, 0
    while i != len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j] and arr[prev] != arr1[i]:
            arr.append(arr1[i])
            i += 1
            prev += 1
            continue
        if arr2[j] < arr1[i] and arr[prev] != arr2[j]:
            arr.append(arr2[j])
            j += 1
            prev += 1
            continue
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    
    while i != len(arr1):
        if arr1[i] != arr[prev]:
            arr.append(arr1[i])
        i += 1
    while j != len(arr2):
        if arr2[j] != arr[prev]:
            arr.append(arr2[j])
        j += 1

    arr.pop(0)
    return arr
    

def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    arr = union_sorted(arr1, arr2)
    print(arr)


if __name__ == "__main__":
    main()