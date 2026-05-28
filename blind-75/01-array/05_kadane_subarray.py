class Solution:
    def kadane(self, arr):
        if not arr:
            return []

        max_sum = curr_sum = arr[0]

        start = end = temp_start = 0

        for i in range(1, len(arr)):

            # Start a new subarray
            if arr[i] > curr_sum + arr[i]:
                curr_sum = arr[i]
                temp_start = i
            else:
                curr_sum += arr[i]

            # Update maximum
            if curr_sum > max_sum:
                max_sum = curr_sum
                start = temp_start
                end = i

        return arr[start:end + 1]


def main():
    arr = list(map(int, input("Enter array elements: ").split()))

    sol = Solution()

    result = sol.kadane(arr)

    print("Maximum Sum Subarray:", result)
    print("Sum:", sum(result))


if __name__ == "__main__":
    main()