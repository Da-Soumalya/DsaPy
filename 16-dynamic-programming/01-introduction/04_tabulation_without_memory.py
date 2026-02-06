# 4. Bottom-up No-memory DP


def fib(n):
    if n < 2: return n

    prev, curr = 0, 1
    for i in range(2, n+1):
        prev, curr = curr, prev+curr
    
    return curr 


print(fib(12)) 

