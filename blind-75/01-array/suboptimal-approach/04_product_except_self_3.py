# intuition: except_self_product at any index equals to the product of all product to its left
# with all products to its right


class Solution():
    def product_except_self(self, nums):
        n = len(nums)
        ans = [1] * n
        
        # Step 1: Calculate Prefix products
        # ans[i] will store the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate Suffix products on the fly
        # Multiply the existing prefix product by the product of everything to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
            
        return ans

def main():
    arr = [7, 1, 5, 3, 6, 4, 7]
    ob = Solution()
    ans = ob.product_except_self(arr)
    print("Input: ", arr)
    print("Output:", ans)

if __name__ == "__main__":
    main()
