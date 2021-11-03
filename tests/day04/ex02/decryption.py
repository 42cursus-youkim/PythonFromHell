def answer(str1, str2):
    lst = [str1, str2]
    ans = ""
    for word in zip(*lst):
        ans = ans + word[0]
        ans = ans + word[-1]
    print(ans)

# str1 = "오 시북쪽로기대 전라"
# str2 = "후3 동으 병를출하!"
# print(answer(str1, str2))