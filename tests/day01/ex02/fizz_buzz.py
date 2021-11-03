def answer(n):
    if n < 0:
        return ValueError
    for num in range(1, n + 1):
        if not (num % 3):
            print("fizz")
        if not (num % 5):
            print("buzz")
        if (num % 3 and num % 5):
            print(num)

# answer(15)