class Solution:
    def max_prod_kadane(self, arr, n):
        min_end, max_end, global_max = arr[0], arr[0], arr[0]
        for i in range(1, n):
            num = arr[i]
            if num < 0:
                max_end, min_end = min_end, max_end
            max_end = max(num, max_end*num)
            min_end = min(num, min_end*num)
            global_max = max(global_max, max_end)
        return global_max
    
    def max_prod_subarray(self, arr, n):
        max_end = arr[0]
        min_end = arr[0]
        ans = arr[0]

        for i in range(1, n):
            num = arr[i]

            # If number is negative, swap
            if num < 0:
                max_end, min_end = min_end, max_end
            
            max_end = max(num, max_end * num)
            min_end = min(num, min_end * num)
            ans = max(ans, max_end)
        return ans


def main():
    # arr = list(map(int, input("Enter an array: ").split()))
    arr = [1, 2, -3, 0, -4, -5]
    sol = Solution()
    answer = sol.max_prod_subarray(arr, len(arr))
    print(answer)


if __name__ == "__main__":
    main()


'''
    This problem has got 2 optimal approach to solve it.
'''