from math import gcd
def answer(num1, num2):
    print(f"gcd : {gcd(num1, num2)}")
    print(f"lcm : {int(num1*num2/gcd(num1, num2))}")

# answer(38 ,152)