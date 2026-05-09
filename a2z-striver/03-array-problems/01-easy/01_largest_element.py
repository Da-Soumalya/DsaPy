class Solution:
    def largest_element(self, arr, n):
        max_val = float('-inf') # avoid naming the identifier as 'max', as it shadows the max() function
        for i in range(n):
            if arr[i] > max_val:
                max_val = arr[i]
        return max_val


def main():
    arr = list(map(int, input("Enter an array of numbers: ").split()))
    sol = Solution()
    answer = sol.largest_element(arr, len(arr))
    print(f"Largest element in the array: {answer}\n")


if __name__ == "__main__":
    main()


'''
# other way to initialize the smallest value to a variable.

import sys
max_val = -sys.maxsize - 1
'''