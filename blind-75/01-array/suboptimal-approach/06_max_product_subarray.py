class Solution:
    def max_prod_subarray(self, arr, n):
        subarray_prods = [1] * ((n*(n+1))//2) # these many subarrays should be present
        ind = 0
        for i in range(len(arr)):
            temp_prod = 1
            for j in range(i, len(arr)):
                temp_prod *= arr[j]
                subarray_prods[ind] = temp_prod
                ind += 1
        max_prod = max(subarray_prods)
        #print(subarray_prods)
        return max_prod


def main():
    # arr = list(map(int, input("Enter an array: ").split()))
    arr = [1, 2, -3, 0, -4, -5]
    sol = Solution()
    answer = sol.max_prod_subarray(arr, len(arr))
    print(answer)


if __name__ == "__main__":
    main()


'''

'''