class Solution:
    def sort(self, arr, n):
        for i in range(n):
            for j in range(n-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


def main():
    arr = list(map(int, input("Enter number separated by spaces: ").split(" ")))
    sol = Solution()
    sorted_arr = sol.sort(arr, len(arr))
    print(f"Sorted array: {sorted_arr}\n")


if __name__ == "__main__":
    main()

'''
study by yourself, why (n-1) and (n-i-1) in the inner loop works as well.
'''