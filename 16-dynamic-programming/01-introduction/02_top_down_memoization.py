# 2. Top-down DP (Memoization)


def fib(n):
    memo = {0:0, 1:1} # using a cache

    def fib(n):
        if n in memo:
            return memo[n]
        
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    return fib(n)


n = 10
print(fib(n))