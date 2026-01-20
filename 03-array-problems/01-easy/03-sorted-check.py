class Solution:
    def check_if_sorted(self, arr, n):
        if n == 1 or n == 2:
            return True
        i = 0
        while(True): # could have run the loop for n times. But helps to check if we missed any scenario
            if i == n-1:
                return True
            if(arr[i] == arr[i+1]):
                i += 1
                continue
            if arr[i] < arr[i+1]:
                for j in range(i, n-1):
                    if arr[j] > arr[j+1]:
                        return False
                return True
            else:
                for j in range(i, n-1):
                    if arr[j] < arr[j+1]:
                        return False
                return True


def main():
    arr = list(map(int, input("Enter an array of numbers: ").split()))
    sol = Solution()
    answer = sol.check_if_sorted(arr, len(arr))
    print("The array is " + ("sorted" if (answer == True) else "not sorted" ))


if __name__ == "__main__":
    main()


'''
    checked for both ascending and descending sort.
'''