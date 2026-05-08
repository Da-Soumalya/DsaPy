'''
goal is to print the next array in the possible dictionary order
'''


class Solution():
    def find_next_permutation(self, arr):
        asc_index = None
        for i in range(len(arr)-2, -1, -1):
            if arr[i] < arr[i+1]:
                asc_index = i
                break
        if asc_index == None:
            arr.reverse()
            return
        for i in range(len(arr)-1, asc_index, -1):
            if arr[asc_index] < arr[i]:
                arr[asc_index], arr[i] = arr[i], arr[asc_index]
                break
        arr[asc_index + 1:] = reversed(arr[asc_index + 1:])


def main():
    arr = [2, 1, 5, 4, 3, 0, 0]
    ob = Solution()
    print(f"The array: {arr}")
    ob.find_next_permutation(arr)
    print(f"The next permutation is: {arr}")


if __name__ == "__main__":
    main()


"""
so, for all possible permutations, unique arrangements of a N sized array is N!
We have attempted the efficient approach to solve this scenario.
"""