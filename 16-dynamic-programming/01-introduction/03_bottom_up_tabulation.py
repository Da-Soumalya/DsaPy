# 3. Bottom-up DP (Tabulation)


def fib(n):
    dp = [0, 1]

    for i in range(2, n+1):
        new = dp[i-2] + dp[i-1]
        dp.append(new) 
    
    return dp[n]


print(fib(11))


# not faster than recursion time complexity wise, but a computer does it faster than a recursion??
# popular quote: every iteration could be turned into iteration and vice-versa. (myth or fact?)