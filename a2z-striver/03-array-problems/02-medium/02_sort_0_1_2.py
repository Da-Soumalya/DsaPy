# Dutch National Flag Algorithm

class Solution():
    def sort_0_1_2(self, arr):
        low, mid, high = 0, 0, len(arr)-1
        while mid <= high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            elif arr[mid] == 2:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr


def main():
    arr = [1, 0, 2, 1, 0, 0, 2]
    ob = Solution()
    print(f"Array before sort: {arr}"
          f"Array after sort: {ob.sort_0_1_2(arr)}")


if __name__ == "__main__":
    main()