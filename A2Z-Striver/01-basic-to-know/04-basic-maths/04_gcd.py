# the code looks really inefficient, like the micro work wise of finding max and min
def gcd(big, small):
    # gonna write the Euclidean method
    while(big%small != 0):
        big, small = small, big%small
    return small


def main():
    num1, num2 = 25, 10
    # gcd: 5, lcm: 50

    big, small = max(num1, num2), min(num1, num2) # do you really need to find min, if max is found?
    print(gcd(big, small))


if __name__ == "__main__":
    main()


"""
self question:
- other than the Euclidean method, are there other ways of finding the GCD?
"""