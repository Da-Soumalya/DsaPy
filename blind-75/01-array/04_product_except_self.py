# intuition: except_self_product at any index equals to the product of all product to its left
# with all products to its right


class Solution():
    def product_except_self(self, arr):
        n = len(arr)
        ans = [1] * n

        prefix = 1
        for i in range(n):
            ans[i] *= prefix
            prefix *= arr[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= arr[i]
        
        return ans


def main():
    arr = [7, 1, 5, 3, 6, 4, 7] #[5, 1, 3, 2, 7]
    ob = Solution()
    ans = ob.product_except_self(arr)
    print("Input: ", arr)
    print("Output:", ans)

if __name__ == "__main__":
    main()
