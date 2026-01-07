from collections import defaultdict


class Solution:
    def frequency_display(self, arr, n):
        freq_map = defaultdict(int)

        for i in range(n):
            freq_map[arr[i]] += 1
        
        for key, value in freq_map.items():
            print(key, value)


if __name__ == "__main__":
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)

    sol = Solution()
    sol.frequency_display(arr, n)
