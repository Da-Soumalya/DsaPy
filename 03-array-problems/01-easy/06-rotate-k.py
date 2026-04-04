class Solution:
    def left_rotate_k(self, arr, k):
        n = len(arr)
        k %= n

        arr_new = self.reverse(arr[:k]) + self.reverse(arr[k:])
        arr_new = self.reverse(arr_new)

        return arr_new
    
    def reverse(self, arr):
        l = len(arr)
        j = l - 1
        
        for i in range(l // 2):
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        
        return arr


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    ob = Solution()
    result = ob.left_rotate_k(arr, 10)
    print(result)


if __name__ == "__main__":
    main()