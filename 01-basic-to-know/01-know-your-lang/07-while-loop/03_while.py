i = 0
try:
    while i < 3:
        print("Running", i)
        i += 1
finally:
    print("Cleaning up")

# while with try-finally block