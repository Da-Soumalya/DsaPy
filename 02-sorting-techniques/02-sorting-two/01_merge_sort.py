def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array
    """
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged


def merge_sort(arr):
    """
    Attempts merge sort on the provided array.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def main():
    """
    Main function to execute merge sort on user-provided input.
    """
    print("Merge Sort Implementation\n\n")
    arr = list(map(int, input("Enter number separated by spaces: ").split(" ")))
    sorted_arr = merge_sort(arr)
    print(f"Sorted array: {sorted_arr}\n")


if __name__ == "__main__":
    main()