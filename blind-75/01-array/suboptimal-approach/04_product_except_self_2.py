# intuition: except_self_product at any index equals to the product of all product to its left
# with all products to its right


class Solution():
    def product_except_self(self, arr):
        prefix_prod, suffix_prod, ans_arr, prod = [0] * len(arr), [0] * len(arr), [0] * len(arr), 1
        for ind in range(len(arr)):
            prod *= arr[ind]
            prefix_prod[ind] = prod
        prod = 1
        for ind in range(len(arr)-1, -1, -1):
            prod *= arr[ind]
            suffix_prod[ind] = prod
        ans_arr[0], ans_arr[len(arr) - 1] = 0, 0 # seems like assigning correct value to the first and last index might not be simple
        for ind in range(1, len(ans_arr) - 1):
            ans_arr[ind] = prefix_prod[ind-1]*suffix_prod[ind+1]
        return ans_arr


def main():
    arr = [7, 1, 5, 3, 6, 4, 7]
    ob = Solution()
    ans = ob.product_except_self(arr)
    print(arr, ans)


if __name__ == "__main__":
    main()