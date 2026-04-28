class Solution():
    def find_max_profit(self, arr):
        min_price, max_profit = arr[0], 0
        for i in range(1, len(arr)):
            if arr[i] <= min_price: # can't sell on the buying day = 0 gains
                min_price = arr[i]
            else:
                max_profit = max(max_profit, arr[i]-min_price)
        return max_profit


def main():
    arr = [7, 2, 5, 3, 6, 1, 4]
    ob = Solution()
    ans = ob.find_max_profit(arr)
    print(f"Given the stock prices: {arr}\n"
          f"Max profit is: {ans}")


if __name__ == "__main__":
    main()


# the question hasn't asked which day to buy and on which day to sell.