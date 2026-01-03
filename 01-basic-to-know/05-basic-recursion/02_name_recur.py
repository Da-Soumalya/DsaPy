def nameRecur(name, n):
    if n == 1:
        print(name, n)
        return
    n -= 1
    nameRecur(name, n)
    print(name, n)
    return


def main():
    name, n = "Developer", 10
    nameRecur(name, n)


if __name__ == "__main__":
    main()