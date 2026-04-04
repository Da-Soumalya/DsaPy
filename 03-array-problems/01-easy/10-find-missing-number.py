'''
Given an integer array of size n containing distinct values in the range 
from 0 to n (inclusive), return the only number missing from the array within this range.
'''


class Solution():
    def find_missing_num(self, num):
        n, arr_sum = len(num), sum(num)
        tot_sum = (n*(n+1))/2
        return int(tot_sum - arr_sum)



def main():
    num = [0, 1, 2, 4, 5]
    ob = Solution()
    print(ob.find_missing_num(num))


if __name__ == "__main__":
    main()