'''
Problem Statement: Given an integer array nums of size n, 
return the majority element of the array. 

The majority element of an array is an element that 
appears more than n/2 times in the array. The array is guaranteed to have a majority element. 
'''


# Boyer–Moore Voting Algorithm


class Solution():
    def find_majority_element(self, arr):
        count, element = 0, 0
        for num in arr:
            if count == 0:
                element = num
                count = 1
            elif element == num:
                count += 1
            elif element != num:
                count -= 1
        return element


def main():
    arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
    ob = Solution()
    print(f"The majority element in {arr} is: {ob.find_majority_element(arr)}")


if __name__ == "__main__":
    main()