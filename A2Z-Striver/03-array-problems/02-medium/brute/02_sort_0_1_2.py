# Counting-sort problem with 3 counters.

class Solution():
    def sort_0_1_2(self, arr):
        zero_count, one_count, two_count = 0, 0, 0
        for num in arr:
            if num == 0:
                zero_count += 1
            if num == 1:
                one_count += 1
            if num == 2:
                two_count += 1
        for i in range(len(arr)):
            if zero_count > 0:
                arr[i] = 0
                zero_count -= 1
            elif one_count > 0:
                arr[i] = 1
                one_count -= 1
            else:
                arr[i] = 2
        return arr


def main():
    arr = [1, 0, 2, 1, 0, 0, 2]
    ob = Solution()
    print(f"Array before sort: {arr}"
          f"Array after sort: {ob.sort_0_1_2(arr)}")


if __name__ == "__main__":
    main()