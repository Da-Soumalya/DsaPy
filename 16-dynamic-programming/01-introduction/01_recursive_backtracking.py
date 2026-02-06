# 1. Recursive backtracking

def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    return fib(n-1) + fib(n-2)


n = 9
print(fib(n))


# Time: O(2^N)
# Recursive Backtracking DP: Nth fibonacci number