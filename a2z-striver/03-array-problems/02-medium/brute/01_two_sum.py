class Solution:
    def two_sum_exists(self, arr, n, target):
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] == target:
                    return "YES" # return f"YES at ({i} {j})"
        return "NO"

    
    def two_sum_indices(self, arr, n, target):
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] == target:
                    return f"({i} {j})"
        return "(-1 -1)"


def main():
    arr = list(map(int, input("Enter an array of numbers: ").split()))
    target = int(input("Enter the target sum: "))
    sol = Solution()
    print(sol.two_sum_exists(arr, len(arr), target))
    print(sol.two_sum_indices(arr, len(arr), target))


if __name__ == "__main__":
    main()


'''
    Two variants of the same problem: YES/NO, indices
'''