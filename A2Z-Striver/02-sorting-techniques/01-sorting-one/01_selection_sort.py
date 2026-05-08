class Solution:
    def sort(self, arr, n):
        for i in range(n):
            for j in range(i, n):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr


def main():
    arr = list(map(int, input("Enter number separated by spaces: ").split(" ")))
    sol = Solution()
    sorted_arr = sol.sort(arr, len(arr))
    print(f"Sorted array: {sorted_arr}\n")


if __name__ == "__main__":
    main()

'''
classical selection sort does not perform multiple swaps per inner loop.
Why that is more efficient, and why both works
- study
'''