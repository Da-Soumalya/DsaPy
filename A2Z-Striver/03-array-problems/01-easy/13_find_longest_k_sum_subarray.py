'''
Problem Statement: Given an array nums of size n and an integer k, find the 
length of the longest sub-array that sums to k. If no such sub-array exists, return 0. 
'''


class Solution():
    def find_longest_k_sum_subarray(self, arr, k):
        left, right, max_length, subarray_sum = 0, 0, 0, 0
        for i in range(len(arr)):
            subarray_sum += arr[i]
            right += 1
            if subarray_sum == k:
                max_length = max(max_length, right-left)
            if subarray_sum > k:
                subarray_sum -= arr[left]
                left += 1
        return max_length


def main():
    arr = [10, 5, 2, 7, 1, 9]
    k = 15
    ob = Solution()
    ans = ob.find_longest_k_sum_subarray(arr, k)
    print(F"Given this array: {arr}\n"
          F"The length of the longest subarray which returns the sum {k} is {ans}")


if __name__ == "__main__":
    main()


# formatted string literal. 'F' upper f works as well like the lower case one.
"""
return -1 if max_length == 0 else max_length

if we were asked to return -1, if no such subarrays were found whose sum 
returned to k.
"""

"""
Example test case: where this approach fails:
arr = [1, -1, 5, -2, 3]
k = 3

left pointer windows is asked to shrink when at the 3rd iteration 5(>k) is encountered.

So, the real deal is do we consider negative integers as valid list elements?
(if yes, consider using a prefix-sum + hashmap approach)
"""