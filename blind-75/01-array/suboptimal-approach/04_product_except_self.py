class Solution():
    def product_except_self(self, arr):
        prod, ans = 1, [0]*len(arr)
        for num in arr:
            prod *= num
        for ind in range(len(ans)):
            ans[ind] = prod//arr[ind]
        return ans


def main():
    arr = [7, 1, 5, 3, 6, 4, 7]
    ob = Solution()
    ans = ob.product_except_self(arr)
    print(arr, ans)


if __name__ == "__main__":
    main()