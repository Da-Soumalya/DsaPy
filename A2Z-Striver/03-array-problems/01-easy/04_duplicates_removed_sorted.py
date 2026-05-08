# to remove duplicates from a SORTED array.

def main():
    arr = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7]

    answer_arr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer_arr.append(arr[i])
    print(answer_arr)


if __name__ == "__main__":
    main()

