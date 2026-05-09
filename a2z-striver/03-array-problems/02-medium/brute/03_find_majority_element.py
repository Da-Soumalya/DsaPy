'''
Problem Statement: Given an integer array nums of size n, 
return the majority element of the array. 

The majority element of an array is an element that 
appears more than n/2 times in the array. The array is guaranteed to have a majority element. 
'''


# I am not sure, if I'll need defaultdict as was used in basic hashing.


class Solution():
    def find_majority_element(self, arr):
        freq = {}
        # for num in arr:
        #     if num not in freq:
        #         freq[num] = 1
        #     else:
        #         freq[num] += 1
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        ans = max(freq, key=freq.get)
        return ans


def main():
    arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
    ob = Solution()
    print(f"The majority element in {arr} is: {ob.find_majority_element(arr)}")


if __name__ == "__main__":
    main()