'''
Given a number of stairs(n), we can make 1 step or 2 steps at a turn. How many distinct ways
are there to climb the n stairs.
'''
# used a bottom-up approach for this solution


class Solution:
    def dp(self, n):
        dp = [-1]*(n+2)

        dp[0], dp[1] = 0, 1
        for i in range(2, n+2):
            dp[i] = dp[i-1] + dp[i-2]
        
        #print(dp)
        return dp[n+1]


def main():
    n = int(input("Enter the number of stairs: "))
    ob = Solution()
    answer = ob.dp(n)
    print(f"There are {answer} ways to climb {n} stairs")


if __name__ == "__main__":
    main() 