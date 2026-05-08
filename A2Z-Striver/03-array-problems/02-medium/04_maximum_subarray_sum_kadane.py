class Solution:
    def kadane(self, arr, n):
        max_sum = curr_max = arr[0]
        for i in range(1, n):
            curr_max = max(arr[i], curr_max+arr[i])
            max_sum = max(max_sum, curr_max)
        return max_sum


def main():
    arr = list(map(int, input("Enter an array: ").split()))
    sol = Solution()
    answer = sol.kadane(arr, len(arr))
    print(answer)


if __name__ == "__main__":
    main()


'''

'''