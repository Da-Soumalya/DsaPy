class Solution():
    def check_duplicate(self, arr):
        arr_len, set_len = len(arr), len(set(arr))
        if arr_len == set_len:
            return False
        else:
            return True


def main():
    arr = [7, 1, 5, 3, 6, 4, 7]
    ob = Solution()
    ans = ob.check_duplicate(arr)
    print(ans)


if __name__ == "__main__":
    main()