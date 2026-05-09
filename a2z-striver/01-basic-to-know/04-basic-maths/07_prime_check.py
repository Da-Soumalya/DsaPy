def check_prime(num):
    if num < 2:
        return False
    for i in range(2, num**0.5):
        if num%i == 0:
            return False
    return True


def main():
    num = int(input("Enter a number: "))
    if check_prime:
        print(num, " is a Prime number.")
    else:
        print(f"{num} is not an Prime number.")


if __name__ == "__main__":
    main()