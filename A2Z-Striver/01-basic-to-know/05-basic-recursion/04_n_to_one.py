def recurPrint(n):
    if n == 0:
        return
    print(n)
    recurPrint(n-1)


def main():
    n = 10
    recurPrint(n)


if __name__ == "__main__":
    main()