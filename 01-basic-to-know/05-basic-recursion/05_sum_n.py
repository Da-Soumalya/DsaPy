# yeah, not used: (num*(num+1))//2


def sumRecur(n, start=1, sum=0):
    if start == n:
        sum += start
        return sum
    return sumRecur(n, start+1, sum+start)


def main():
    n = 10
    print(sumRecur(n))


if __name__ == "__main__":
    main()