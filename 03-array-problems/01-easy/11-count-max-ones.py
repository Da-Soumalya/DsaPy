'''
Problem Statement: Given an array that contains only 1 and 0 
return the count of maximum consecutive ones in the array..
'''


class Solution():
    def count_max_ones(self, arr):
        curr_max, prev_max = 0, 0
        for num in arr:
            if num == 0:
                curr_max = 0
            else:
                curr_max += 1
                prev_max = max(prev_max, curr_max)
        return prev_max


def main():
    arr = [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    obj = Solution()
    ans = obj.count_max_ones(arr)
    print(f"The maximum number of ones in this array: \n{arr}"
          f" is = {ans}" )


if __name__ == "__main__":
    main()