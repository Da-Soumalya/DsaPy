class Solution():
    def two_sum_exist(self, arr, req_sum):
        sorted_arr = sorted(arr) # doesn;t require the use of extra space, but using it for the next method
        left, right = 0, len(sorted_arr)-1
        while left < right:
            if sorted_arr[left] + sorted_arr[right] < req_sum:
                left += 1
            elif sorted_arr[left] + sorted_arr[right] > req_sum:
                right -= 1
            else:
                return "YES"
        return "NO"

    def two_sum_indices(self, arr, req_sum):
        maped_arr = {}
        for ind, num in enumerate(arr):
            complementary_ele = req_sum - num
            if complementary_ele in maped_arr:
                return [maped_arr[complementary_ele], ind]
            maped_arr[num] = ind
        return [-1, -1]

def main():
    arr = [2, 6, 5, 8, 11]
    target = 14
    ob = Solution()
    ans = ob.two_sum_exist(arr, target)
    ans_2 = ob.two_sum_indices(arr, target)
    print(ans, ans_2)


if __name__ == "__main__":
    main()