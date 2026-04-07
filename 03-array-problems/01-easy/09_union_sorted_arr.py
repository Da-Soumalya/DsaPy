'''
Input: n = 10, m = 7, arr1[] = {1,2,3,4,5,6,7,8,9,10} arr2[] = {2,3,4,4,5,11,12}
'''

def union_sorted(arr1, arr2):
    i, j = 0, 0
    arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if not arr or arr[-1] != arr1[i]:
                arr.append(arr1[i])
            i += 1
            j += 1

        elif arr1[i] < arr2[j]:
            if not arr or arr[-1] != arr1[i]:
                arr.append(arr1[i])
            i += 1

        else:
            if not arr or arr[-1] != arr2[j]:
                arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        if not arr or arr[-1] != arr1[i]:
            arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not arr or arr[-1] != arr2[j]:
            arr.append(arr2[j])
        j += 1

    return arr
    

def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    arr = union_sorted(arr1, arr2)
    print(arr)


if __name__ == "__main__":
    main()