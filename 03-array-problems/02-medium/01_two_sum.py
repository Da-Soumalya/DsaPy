class Solution:
    def two_sum(self, arr, n, target):
        arr.sort()
        i, j = 0, n-1
        while i < j:
            if arr[i] + arr[j] == target:
                return "YES"
            if arr[i] + arr[j] > target:
                j -= 1
                continue
            if arr[i] + arr[j] < target:
                i += 1
        return "NO"
    

    # used a hashmap instead of an extra array
    def two_sum_indices(self, arr, target):
        mp = {}  # Dictionary to store element -> index
        for i, num in enumerate(arr):
            complement = target - num
            # If complement found, return indices
            if complement in mp:
                return [mp[complement], i]
            # Store current element and index
            mp[num] = i
        # No pair found
        return [-1, -1]




def main():
    arr = list(map(int, input("Enter an array of numbers: ").split()))
    target = int(input("Enter the target sum: "))
    sol = Solution()
    answer = sol.two_sum(arr, len(arr), target)
    print(answer)


if __name__ == "__main__":
    main()


'''
    two-pointer greedy technique, most optimal for YES/NO variant
    for indices we end up using extra space.
'''