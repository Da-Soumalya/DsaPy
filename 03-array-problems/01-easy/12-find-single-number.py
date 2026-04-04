'''
Problem Statement: Given a non-empty array of integers arr, every element appears 
twice except for one. Find that single one.
'''


class Solution():
    def only_single_number(self, arr):
        result = 0
        for num in arr:
            result ^= num
        return result


def main():
    arr = [1, 1, 5, 5, 3, 9, 3, 6, 9, 2, 2]
    ob = Solution()
    ans = ob.only_single_number(arr)
    print(f"The only single number among the couples in the array is: \n{arr}"
          f" is = {ans}")


if __name__ == "__main__":
    main()


# this problem extends to bit manipulation, if every elements occured thrice instead of twice.