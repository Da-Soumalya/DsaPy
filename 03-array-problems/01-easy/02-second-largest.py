class Solution:
    def largest_element(self, arr, n):
        max_val = second_max = float('-inf') 
        for i in range(n):
            if arr[i] > max_val:
                second_max, max_val = max_val, arr[i]
        return second_max


def main():
    arr = list(map(int, input("Enter an array of numbers: ").split()))
    sol = Solution()
    answer = sol.largest_element(arr, len(arr))
    print(f"Second largest element in the array: {answer}\n")


if __name__ == "__main__":
    main()


'''

'''