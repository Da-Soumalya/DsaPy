class Solution():
    def find_max_profit(self, arr):
        temp_ans, ans = 0, 0
        for i in range(len(arr)):
            temp = arr[i]
            for j in range(i+1, len(arr)):
                if arr[j] > arr[i]:
                    temp = max(arr[j], temp)
            temp_ans = temp - arr[i]
            ans = max(ans, temp_ans)
        return ans


def main():
    arr = [7, 1, 5, 3, 6, 4]
    ob = Solution()
    ans = ob.find_max_profit(arr)
    print(f"Given the stock prices: {arr}\n"
          f"Max profit is: {ans}")


if __name__ == "__main__":
    main()