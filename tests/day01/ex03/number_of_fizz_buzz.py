def answer(n):
    if n < 0:
        return ValueError
    if n == 0:
        print(1)
        print(2)
        return
    fizz = 0
    buzz = 0
    num = 1
    while (fizz != n or buzz != n):
        if not (num % 3 or fizz == n):
            print("Fizz")
            fizz += 1
        elif (num % 3 == 0 and fizz == n):
            print(num)
        if not (num % 5 or buzz == n):
            print("Buzz")
            buzz += 1
        elif (num % 5 == 0 and buzz == n):
            print(num)
        if (num % 3 and num % 5):
            print(num)
        num += 1

# answer(0)