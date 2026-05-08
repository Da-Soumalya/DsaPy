i, s = 1, 6
for _ in range(4):
    for j in range(1, i+1):
        print(j, end="")
    print(" "*s, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    i += 1
    s -= 2
    print("")

'''
1      1
12    21
123  321
12344321
'''