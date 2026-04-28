'''
Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and 
negative elements. Without altering the relative order of positive and negative elements, 
you must return an array of alternately positive and negative values.
'''


class Solution():
    def rearrange_element(self, arr):
        n = len(arr)
        ans_arr = [0] * n
        pos, neg = 0, 1
        for i in range(n):
            if arr[i] < 0: # negative
                ans_arr[neg] = arr[i]
                neg += 2
            else:
                ans_arr[pos] = arr[i]
                pos += 2
        return ans_arr            


def main():
    arr = [1, 2, -3, -1, -2, 3]
    ob = Solution()
    print("Array before arranging: ", arr)
    ans = ob.rearrange_element(arr)
    print(f"Array after arranging: {ans}")


if __name__ == "__main__":
    main()


# Inference: arr length will always be even, since we are guranteed to have equal number of
# postive and negative elements. Zero will never be present in the array.
#
# The question could've be twisted in ways like: odd length, zero inclusion, etc...
# btw, is it always like (pos, neg...) or it could be (neg, pos...)? - in the examples
# where the brute and efficient algorithms are mentioned. It is said to start with positive 
# elements first.