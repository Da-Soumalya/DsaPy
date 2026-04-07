class Solution():
    def find_longest_zero_sum_subarray(self, arr):
        prefix_map = {}
        current_sum = 0
        max_length = 0

        for i in range(len(arr)):
            current_sum += arr[i]

            # Case 1: sum becomes 0 from start
            if current_sum == 0:
                max_length = i + 1

            # Case 2: sum seen before
            if current_sum in prefix_map:
                length = i - prefix_map[current_sum]
                max_length = max(max_length, length)
            else:
                # store first occurrence only
                prefix_map[current_sum] = i

        return max_length


def main():
    arr = [9, -3, 3, -1, 6, -5]
    ob = Solution()
    ans = ob.find_longest_zero_sum_subarray(arr)
    print(f"Given the array: {arr}\n"
          f"The size of longest zero sum subarray is: {ans}")


if __name__ == "__main__":
    main()