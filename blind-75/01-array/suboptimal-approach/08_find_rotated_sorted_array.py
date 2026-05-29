class Solution():
    def find_ele_my_initial_approach(self, arr, key): # requiring 2 binary searches
        n = len(arr)
        low, high = 0, n-1
        while(low < high):
            mid = (low + high) // 2
            if arr[mid] < arr[high]: # min should either be mid or at the left of it
                high = mid
            else:
                low = mid + 1
        min_ind, max_ind = low, low-1
        pseudo_min, pseudo_max = min_ind - low, max_ind + low -1
        while(pseudo_min <= pseudo_max):
            mid = (pseudo_min + pseudo_max) // 2
            rotated_mid = (mid + low) % n
            if arr[rotated_mid] == key:
                return rotated_mid
            elif arr[rotated_mid] < key:
                pseudo_min = mid + 1
            else:
                pseudo_max = mid - 1
        return -1
    
    def find_ele(self, arr, key):
        n = len(arr)

        # Step 1: Find rotation index (minimum element)
        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] < arr[high]:
                high = mid
            else:
                low = mid + 1

        rotation = low

        # Step 2: Binary search on virtual sorted array
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            # Convert virtual index -> actual rotated index
            real_mid = (mid + rotation) % n

            if arr[real_mid] == key:
                return real_mid
            elif arr[real_mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return -1


def main():
    arr = [4, 5, 6, 7, 0, 1, 2]
    k = 6
    ob = Solution()
    ans = ob.find_ele(arr, k)
    print(f"In the array: {arr},\nThe value {k} is found in index: {ans}")


if __name__ == "__main__":
    main()