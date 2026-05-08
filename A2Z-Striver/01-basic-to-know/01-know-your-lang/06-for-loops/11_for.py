def gen():
    for i in range(3):
        yield i

for val in gen():
    print(val)

# using generator or iterable