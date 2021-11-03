def answer(num):
    if num < 0:
        return ValueError
    for i in range(num):
        print(' ' * (num - i) + '*' * (2 * i + 1))

# answer(5)
