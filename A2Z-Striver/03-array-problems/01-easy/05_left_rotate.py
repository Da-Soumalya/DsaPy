def main():
    arr = [1, 2, 3, 4, 5]
    arr.append(arr.pop(0))
    print(arr)


if __name__ == "__main__":
    main()