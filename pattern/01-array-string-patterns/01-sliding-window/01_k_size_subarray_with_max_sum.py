class Solution():
    def find_answer(self, arr, k):
        window_sum = 0
        for i in range(k):
            window_sum += arr[i]
        ans = window_sum
        for i in range(1, len(arr)-k+1):
            window_sum = window_sum - arr[i-1] + arr[i+k-1]
            ans = max(window_sum, ans)
        return ans 


def main():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    ob = Solution()
    ans = ob.find_answer(arr, k)
    print(f"In the array: {arr}.\n"
          f"The maximum sum if subarray size was {k} is: {ans}")


if __name__ == "__main__":
    main()