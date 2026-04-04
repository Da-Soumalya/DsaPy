def remove_zeroes(arr):
    zero_count = 0
    zero_positions = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_positions.append(i)
            zero_count += 1
    update = 0
    for val in zero_positions:
        arr.pop(val - update)
        update += 1
    arr.extend([0]*zero_count)
    print(arr)


if __name__ == "__main__":
    arr = [1, 0, 2, 3, 0, 4, 0, 1]
    remove_zeroes(arr)

# it is supposedly best done with a two-pointer approach.