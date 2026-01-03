def factRecur(n, start=1, fact=1):
    if(start == n):
        fact *= start
        return fact
    return factRecur(n, start+1, fact*start)


def main():
    n = 5
    print(factRecur(n))


if __name__ == "__main__":
    main()