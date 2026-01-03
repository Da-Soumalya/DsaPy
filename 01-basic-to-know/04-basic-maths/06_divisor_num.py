def find_divisor(num):
    divisors = set()
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            divisors.add(i)
            divisors.add(num//i)
    return divisors


def main():
    num = int(input("Enter a number: "))
    print(find_divisor(num))


if __name__ == __main__:
    main()