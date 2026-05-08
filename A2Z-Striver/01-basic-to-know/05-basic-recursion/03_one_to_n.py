# let's print 1 to n


def recurPrint(n):
    if n == 1:
        print(n)
        return
    n -= 1
    recurPrint(n)
    print(n+1)
    return


def main():
    n = 10
    recurPrint(n)


if __name__ == "__main__":
    main()


'''

def recurPrint(n, current=1):
    if current > n: # Base case: stop when current exceeds n
        return
    print(current)  # Print the current value
    recurPrint(n, current + 1)  # Recursive call with current incremented by 1
'''
# concept of default argument used