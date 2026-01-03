def should_continue(x):
    return x < 5

i = 0
while should_continue(i):
    print(i)
    i += 1

# while with condition coming from a function