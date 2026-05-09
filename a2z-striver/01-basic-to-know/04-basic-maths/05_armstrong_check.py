def is_armstrong(num):
    l, s, n = len(str(num)), 0, num
    while n != 0:
        s += (n%10)**l
        n //= 10
    if s == num:
        return True
    return False


def main():
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print(num, " is an armstrong number.")
    else:
        print(f"{num} is not an armstrong number.")


if __name__ == "__main__":
    main()


'''
About Armstrong or Narcisistic numbers.

One whose, sum of each digits powered by the number of digits, 
returns the number itself.
example: 153, 370, 371, 9474, 54748, 92727, ...
'''