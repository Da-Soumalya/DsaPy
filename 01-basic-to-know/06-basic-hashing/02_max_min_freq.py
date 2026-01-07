from collections import defaultdict


class Solution:
    def find_max_min_freq(self, arr, n):
        freq_map = defaultdict(int)

        for i in range(n):
            freq_map[arr[i]] += 1
        
        max_freq_element = max(freq_map, key=freq_map.get)
        min_freq_element = min(freq_map, key=freq_map.get)

        print(f"The element {max_freq_element} appears {freq_map[max_freq_element]} times (max).\n"
              f"The element {min_freq_element} appears {freq_map[min_freq_element]} times (min).")


def main():
    arr = [2, 2, 3, 4, 4, 2]
    n = len(arr)

    sol = Solution()
    sol.find_max_min_freq(arr, n)


if __name__ == "__main__":
    main()
