def nForest(n: int) -> None:
    for i in range(1, n+1):
        print(*range(1, i + 1))

nForest(5)

# print(" ".join(map(str, range(1, i + 1))))
# the variant also works when formatting is a concern.