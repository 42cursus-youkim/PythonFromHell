def answer(oper, num_list):
    ans = 0
    if oper == '+':
        for num in num_list:
            ans += num
    elif oper == '-':
        for num in num_list:
            ans -= num
    elif oper == '*':
        for num in num_list:
            ans *= num
    elif oper == '/':
        for num in num_list:
            ans /= num
    else:
        return ValueError
    print(ans)

# answer('+', [1,2,3,4,5,6,7])