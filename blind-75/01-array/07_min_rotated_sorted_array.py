class Solution():
    def find_min(self, arr):
        n = len(arr)
        low, high = 0, n-1
        while(low < high):
            mid = (low + high) // 2
            if arr[mid] < arr[high]: # min should either be mid or at the left of it
                high = mid
            else:
                low = mid + 1
        return arr[low]


def main():
    arr = [4, 5, 6, 7, 0, 1, 2]
    ob = Solution()
    ans = ob.find_min(arr)
    print(f"In the array: {arr}\nThe minimum number is: {ans}")


if __name__ == "__main__":
    main()


'''
arr = [5, 5, 5, 5] does work here as well

'''