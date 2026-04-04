'''
Problem Statement: Given a non-empty array of integers arr, every element appears 
twice except for one. Find that single one.
'''


class Solution():
    def only_single_number(self, arr):
        new_arr = sorted(arr) # to avoid the n^n bruteforce
        for i in range(1, len(new_arr)-1):
            if new_arr[i] != new_arr[i+1] and new_arr[i] != new_arr[i-1]:
                return new_arr[i]


def main():
    arr = [1, 1, 5, 5, 3, 9, 3, 6, 9, 2, 2]
    ob = Solution()
    ans = ob.only_single_number(arr)
    print(f"The only single number among the couples in the array is: \n{arr}"
          f" is = {ans}")


if __name__ == "__main__":
    main()

# this logic fails if the input was [1, 1, 2]