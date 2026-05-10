class Solution():
    def find_max_profit(self, arr):
        min_cost, max_profit = arr[0], 0
        for i in range(1, len(arr)):
            if arr[i] < min_cost: # can't sell in the day, when it is bought
                min_cost = arr[i] 
            else:    
                max_profit = max(max_profit, arr[i] - min_cost)
        return max_profit


def main():
    arr = [7, 1, 5, 3, 6, 4]
    ob = Solution()
    ans = ob.find_max_profit(arr)
    print(ans)


if __name__ == "__main__":
    main()